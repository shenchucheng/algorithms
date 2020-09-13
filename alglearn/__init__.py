#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/12 Sat

# DESCRIPTION:
# 根据学习要求爬取leetcode题目描述，转化成markdown格式
# 将leetcode markdown文档插入生成的ipynb文档
 

import os, logging

from .tools import load_logger
from .leetcode import get_problem_by_url, get_problem_by_slug
from .leetcode import parse_problem, make_question_md
from .template import Notebook, Cells, Cell, markdowncell, codecell, rawcell


def leetcode_notebook(url: str, filename: str = '', pathDir: str = './leetcode/ipynb',
    cover = False, logConfig: str = './log.json' ):
    load_logger(logConfig)
    logger = logging.getLogger('leetcode-notebook')
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)
    if '/' not in url:
        # slug
        slug = url
    else:
        slug = url.rstrip('/').rsplit('/')[-1]
    try:
        data = get_problem_by_slug(slug)
        data = parse_problem(data)
        questionId = data['questionId']
        if not filename:
            filename = '{}-leetcode-{}.ipynb'.format(questionId, slug)
        book = Notebook(filename, pathDir)
        cell = markdowncell()
        cell['source'] = make_question_md(data)
        book.cells.append(cell)
        cell = codecell()
        cell['source'] = data['codeSnippetspython3']
        # sampleTestCase
        book.cells.append(cell)
        book.cells.append(markdowncell())
        book.save(cover=cover)
    except Exception:
        logger.error('Failed to Create Leetcode Notebook', exc_info=True)