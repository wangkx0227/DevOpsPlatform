import os
import logging
from logging.handlers import RotatingFileHandler

# 日志格式
LOG_NAME = 'devops'
# 日志格式：日期 - 日志名称 - 等级 - 模块名（函数文件名称） - 函数名 - 信息
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(module)s.py - %(funcName)s  - %(message)s "
# 日志路径
LOG_BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR_PATH = os.path.join(LOG_BASE_PATH,'logs')


def create_logger():
    # 创建日志记录器
    logger = logging.getLogger(LOG_NAME)
    logger.setLevel(logging.INFO)

    # 路径，保留5份日志，超过5M切割日志，验证创建文件。
    if not os.path.exists(LOG_DIR_PATH):
        os.mkdir(LOG_DIR_PATH)
    log_path = os.path.join(LOG_DIR_PATH,'app.log')
    file_handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=5)
    file_handler.setLevel(logging.INFO)

    # 创建日志格式器并定义日志格式
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    return logger
