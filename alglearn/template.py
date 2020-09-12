#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/10 Thu

# DESCRIPTION: the template cell for jupyter notebook


import os, json
import logging

from nbformat.v4 import new_markdown_cell, new_code_cell, new_raw_cell, new_notebook
from nbformat.v4.nbbase import validate


logger = logging.getLogger('leetcode-notebook')
CELLKTYPE = ['code', 'markdown', 'raw']
CELLVALID = {
    'cell_type': str,
    'metadata': dict,
    'outputs': list,
    'source': list
}


def cell_valid(k, v ):
    """验证cell键值对有效性
    Returns:
        [type]: 注意：无效时，返回有效数据类型
    """
    if k in CELLVALID.keys() and type(v) != CELLVALID[k]:
        return CELLVALID[k]


def cell_template(cell_type, **kwargs):
    """生成 cell 模板

    Args:
        cell_type (str): cell类型 code/markdown/raw     
    """
    if cell_type not in CELLKTYPE:
        raise NotImplementedError

    if cell_type == 'code':
        return new_code_cell(**kwargs)
        # return {
        #     'cell_type': 'code',
        #     'execution_count': None,
        #     'metadata': {},
        #     'outputs': [],
        #     'source': []
        # }

    elif cell_type == 'markdown':
        return new_markdown_cell(**kwargs)
        # return {
        #     'cell_type': 'markdown',
        #     'metadata': {},
        #     'source': []
        # }
    
    elif cell_type == 'raw':
        return new_raw_cell(**kwargs)


def valid(cell):
    """检查添加至Cells中的元素是否有效
    """
    if type(cell) is Cell:
       return True 
    else:
        logger.warning('Element of Cells must be {} not {}'.format(Cell, type(cell)))
        raise TypeError(Cells, Cell, type(cell))


class Cells(list):
    """Notebook的cells数据，对cells函数参数进行有效性验证
    """
    def __init__(self, cells=''):
        for cell in cells:
            valid(cell)
        super().__init__(cells)

    def append(self, cell):
        valid(cell)
        super().append(cell)

    def extend(self, cells):
        for cell in cells:
            valid(cell)
        super().extend(cells)
    
    def insert(self, index, cell):
        valid(cell)
        super().insert(index, cell)


class Cell(dict):
    """Notebook的单个cell数据检验，生成对应cell_type模板
       模板由.template中加载，cell_type类型应该包含在模板中
    """
    def __init__(self, cell_type: str = 'code', **kwargs):
        cell_init = cell_template(cell_type=cell_type, **kwargs)
        super().__init__(**cell_init)

    def __setitem__(self, k, v):
        t = cell_valid(k, v)
        if t:
            logger.error('Type of {} must be {} not {}'.format(k, t, type(v)))
            raise TypeError(k, t, type(v))
        super().__setitem__(k, v) 


def markdowncell(**kwargs):
    return Cell(cell_type='markdown', **kwargs)


def codecell(**kwargs):
    return Cell(cell_type='code', **kwargs)


def rawcell(**kwargs):
    return Cell(cell_type='raw', **kwargs)


class Notebook:
    def __init__(self, filename: str, pathDir: str = '.', **kwargs):
        if not filename.endswith('.ipynb'):
            filename += '.ipynb'
        self.filename = filename
        self.pathDir = pathDir
        self.filepath = os.path.join(pathDir, filename)
        if 'cells' not in kwargs.keys():
            kwargs['cells'] = Cells()
        self.__notebook = new_notebook(**kwargs)

    
    @property
    def cells(self):
        return self.__notebook['cells']

    def save(self, filename: str = '', pathDir: str = '', cover: bool = False):
        """保存成jupyter notebook

        Args:
            filename (str, optional): 文件名不存在时默认文件名保存. Defaults to ''.
            pathDir (str, optional): 保存目录. Defaults to ''.
            conver (bool, optional): 文件若存在是否覆盖. Defaults to False.

        Returns:
            [str bool]: 若创建成功返回
        """
        if not filename:
            filename = self.filename
        if not pathDir:
            pathDir = self.pathDir
        if not os.path.exists(pathDir):
            os.makedirs(pathDir)
        if not filename.endswith('.ipynb'):
            filename += '.ipynb'
        filepath = os.path.join(pathDir, filename)
        if (not cover) and os.path.exists(filepath):
            warn = 'File "{}" was exists already, '.format(filename)
            warn += 'if you wan to cover it, please set cover=True.'
            logger.warning(warn)
        else:
            with open(filepath, mode='w') as f:
                validate(self.__notebook)
                json.dump(self.__notebook, f)
                logger.info('Create Notebook {} Successfully.'.format(filename))
        return filepath
    
    def cell_add(self, cell):
        self.cells.append(cell)
    
    def cell_insert(self, index, cell):
        self.cells.insert(index, cell)
