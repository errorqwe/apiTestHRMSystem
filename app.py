import os

import logging
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HEADERS = {"Content-Type": "application/json"}
ID = None


def init_logging():

    # 创建日志器
    logger = logging.getLogger()

    # 设置日志器等级
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    sh = logging.StreamHandler()

    # 创建文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/ihrm.log",
                                                   when="S",
                                                   interval=10,
                                                   backupCount=3,
                                                   encoding="utf-8")
    # 创建格式添加到格式器中
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'

    formatter = logging.Formatter(fmt)

    # 将格式器添加到处理器
    sh.setFormatter(formatter)

    fh.setFormatter(formatter)

    # 处理器添加到日志器
    logger.addHandler(sh)

    logger.addHandler(fh)


if __name__ == "__main__":

    init_logging()

