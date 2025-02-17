import os
import logging
from logging.handlers import RotatingFileHandler
from devops_app.settings import LOG_NAME, LOG_FORMAT, BASE_PATH


def create_logger():
    # 创建日志记录器
    logger = logging.getLogger(LOG_NAME)
    logger.setLevel(logging.INFO)
    log_dir_path = os.path.join(BASE_PATH, 'logs')
    log_path = os.path.join(log_dir_path, 'app.log')
    file_handler = RotatingFileHandler(log_path, maxBytes=10000, backupCount=5)
    file_handler.setLevel(logging.INFO)

    # 创建日志格式器并定义日志格式
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    return logger
