#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
log日志组件
@version: 1.0
@author: zhaotf
@file: log_utils.py
@time: 2017/8/10 0010 15:49
"""

import logging
import logging.handlers
logging.basicConfig(level=logging.DEBUG)

LOG_FILE = 'hhcf.log'

# 实例化handler
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5,encoding='utf-8')
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
# 实例化formatter
formatter = logging.Formatter(fmt)
# 为handler添加formatter
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info("python 日志：info")

records = {'john': 55, 'tom': 66}
logger.debug("python 日志：DEBUG :$s", records)




def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
