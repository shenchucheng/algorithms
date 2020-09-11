#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/12 Sat

# DESCRIPTION:
# 根据学习要求爬取leetcode题目描述，转化成markdown格式
# 将leetcode markdown文档插入生成的ipynb文档
 

import os, logging

from .leetcode import get_problem_by_url, get_problem_by_slug
from .leetcode import parse_problem, make_question_md
from .template import Notebook, Cells, Cell, markdowncell, codecell, rawcell


def leetcode_note_book(url: str, filename: str = '', pathDir='./leetcode'):
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)
    if '/' not in url:
        # slug
        slug = url
    else:
        slug = url.rstrip('/').rsplit('/')[-1]
        logging.info(slug)
    try:
        data = get_problem_by_slug(slug)
        data = parse_problem(data)
        questionId = data['questionId']
        if not filename:
            filename = '{}-leetcode-{}.ipynb'.format(questionId, slug)
        book = Notebook(filename, pathDir)
        cell = markdowncell()
        cell['source'] = make_question_md(data).splitlines(True)
        book.cells.append(cell)
        return book.save()
    except Exception as e:
        raise e
        logging.warning(e)