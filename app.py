#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/11 Fri

# DESCRIPTION: 
# 根据学习要求爬取leetcode题目描述，转化成markdown格式
# 将leetcode markdown文档插入生成的ipynb文档
# 


import fire

from alglearn import leetcode_notebook


if __name__ == "__main__":
    fire.Fire(leetcode_notebook)
    # leetcode_note_book('https://leetcode-cn.com/problems/two-sum/')
