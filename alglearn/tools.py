#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# AUTHOR: Chucheng Shen
# DATE: 2020/09/12 Sat

# DESCRIPTION: 公用工具


import os, json, logging
import logging.config


# requests 爬虫
UA = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
HEADERS = {'user_agent': UA}


# logging 日志
def load_logger(filepath='./log.json'):
    error = 'Load Logging Config Error:'
    if not os.path.exists(filepath):
        error += ' File "{}" was not exists,'.format(filepath)
        error += ' if you want setup logging by file, please check the path'
        logging.warning(error)
        return
    try:
        with open(filepath, mode='r') as f:
            confiigDict = json.load(f)
            logging.config.dictConfig(confiigDict)
    except json.JSONDecodeError as e:
        logging.critical(error)
        raise e
    except Exception:
        logging.error(error, exc_info=True)