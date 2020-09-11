#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/11 Fri

# DESCRIPTION: 爬取leetcode中国算法题描述


import json

from requests import Session
from markdownify import markdownify as md

from .tools import HEADERS, UA
from .config import MDSTYLE


GRAPHQLHEADERS = HEADERS.copy()
GRAPHQLHEADERS.update({
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Referer': 'https://leetcode-cn.com/problems/all'
    })
session = Session()
session.headers = HEADERS


def leetcode_graphql_querry(data: dict, headers: dict = None) -> dict:
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


def get_problem_by_slug(slug: str) -> dict:
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
                    topicTags {
                        name
                        slug
                        translatedName
                        __typename }
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
    data['content'] = md(data['content'])
    data['translatedContent'] = md(data['translatedContent'])
    return data


def make_question_md(data):
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
    return MDSTYLE.format(**data_dict)
