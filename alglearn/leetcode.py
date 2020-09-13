#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/11 Fri

# DESCRIPTION: 爬取leetcode中国算法题描述


import json, logging

from requests import Session
from markdownify import markdownify as md
from typing import List, Dict

from .tools import HEADERS, UA


logger = logging.getLogger('leetcode-requests')
GRAPHQLHEADERS = HEADERS.copy()
GRAPHQLHEADERS.update({
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Referer': 'https://leetcode-cn.com/problems/all'
    })
session = Session()
session.headers = HEADERS


def leetcode_graphql_querry(data: dict, headers: dict = None) -> Dict:
    """leetcode数据库查询

    Args:
        data (dict): post参数
        headers (dict, optional): 需要构造的特殊请求头. Defaults to None.

    Returns:
        dict: [返回参数]
    """
    url = 'https://leetcode-cn.com/graphql/'
    json_data = json.dumps(data).encode('utf8')
    __headers = GRAPHQLHEADERS.copy()
    if headers:
        __headers.update(headers)
    headers = __headers
    resp = session.post(url, data = json_data, headers = headers, timeout = 10)
    if resp.status_code != 200:
        info = 'Request-error status_code {}, '.format(resp.status_code)
        info += 'Url: {}, data: {}'.format(url, json_data)
        logger.info(info)
    content = resp.json()
    return content


def get_problems_slug():
    """获取题库基本信息

    Returns:
        [type]: [description]
    """
    data = {
        "operationName": "allQuestions",
        "variables": {},
        "query": '''query allQuestions {
            allQuestionsBeta {
                ...questionSummaryFields
                __typename }
            }
            fragment questionSummaryFields on QuestionNode {
                title
                titleSlug
                translatedTitle
                questionId
                questionFrontendId
                status
                difficulty
                isPaidOnly
                categoryTitle
                __typename }
            '''
        }
    return leetcode_graphql_querry(data)  # 数据量1700+


def get_problem_by_slug(slug: str) -> Dict:
    """根据slug 获取对应题目

    Args:
        slug (str): 题目的slug参数，一般为题目名称

    Returns:
        dict: 返回querry对应参数
    """
    params = {
        'operationName': 'questionData',
        'variables': {'titleSlug': slug},
        'query': '''query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) {
                    questionId
                    title
                    titleSlug
                    content
                    translatedTitle
                    translatedContent
                    isPaidOnly
                    difficulty
                    similarQuestions
                    sampleTestCase
                    topicTags {
                        name
                        slug
                        translatedName
                        __typename }
                    codeSnippets {
                        lang
                        langSlug
                        code                        
                        __typename}
                   } }
                 '''
    }
    return leetcode_graphql_querry(params, {'Referer': 'https://leetcode-cn.com/problems/' + slug})



def get_problem_by_url(url: str):
    """根据题库url链接获取题目描述

    Args:
        url (str): url 格式应为 https://leetcode-cn.com/problems/pond-sizes-lcci/
    """
    slug = url.strip('/').split('/')[-1]
    return get_problem_by_slug(slug)


def parse_problem(data):
    data = data['data']['question']
    if type(data['similarQuestions']) == str:
        data['similarQuestions'] = eval(data['similarQuestions'])
    data['content'] = leetcodemd(data['content'])
    data['translatedContent'] = leetcodemd(data['translatedContent'])
    for code in data['codeSnippets']:
        if code['lang'] == 'Python3':
            codes = format_md_source(code['code'])
            codes.insert(0, 'from typing import List, Dict, Tuple')
            data['codeSnippets' + code['langSlug']] = codes 
            break
    return data


def make_question_md(data, template='') -> str:
    """根据模板生成leetcode题目的markdown

    Args:
        data (dict): leetcode题目数据
        template (str, optional): markdown模板字符串. Defaults to ''.

    Returns:
        [str]: 生成的markdown文本
    """
    if not template:
        from .config import MDSTYLE
        template = MDSTYLE
    baseUrl = 'https://leetcode-cn.com/problems/{}/'
    titleSlug = data['titleSlug']
    topicTags = data['topicTags']
    similarQuestions = data['similarQuestions']
    topicTagsZh = '、'.join(i['translatedName'] for i in topicTags)
    topicTags   = '; '.join(i['name'] for i in topicTags)
    for d in similarQuestions:
        d['url'] = baseUrl.format(d['titleSlug'])
    similarQuestionsZh = '、'.join(
        '[*{}*]({})'.format(i['translatedTitle'], i['url']) for i in similarQuestions
        )
    similarQuestions = '; '.join(
        '[*{}*]({})'.format(i['title'], i['url']) for i in similarQuestions
    )
    difficulty = data['difficulty']
    difficultyZh = {'Medium': '中等', 'Hard': '复杂', 'Easy': '简单'}[difficulty]
    data_dict = dict(
    questionId         = data['questionId'],
    title              = data['title'],
    titleZh            = data['translatedTitle'],
    content            = data['content'],
    contentZh          = data['translatedContent'],
    isPaidOnly         = data['isPaidOnly'],
    titleSlug          = titleSlug,
    difficulty         = difficulty,
    difficultyZh       = difficultyZh,
    url                = baseUrl.format(titleSlug),
    topicTags          = topicTags,
    topicTagsZh        = topicTagsZh,
    similarQuestions   = similarQuestions,
    similarQuestionsZh = similarQuestionsZh,
    )
    return format_md_source(template.format(**data_dict))


def format_md_source(string: str) -> List:
    """生成ipynb cell source 对应的格式
    """
    return string.splitlines(True)


def leetcodemd(html: str) -> str:
    """将leetcode的html转化成md，完善markdownify库部分解析

    Args:
        html (str): html源文档
    """ 
    string = md(html)
    string = string.replace('[', '\\[')
    string = string.replace(']', '\\]')
    return string 
