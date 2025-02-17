import os
import logging
from logging.handlers import TimedRotatingFileHandler
from devops_app.settings import LOG_NAME, LOG_FORMAT, BASE_PATH


def create_logger():
    # 创建日志记录器
    logger = logging.getLogger(LOG_NAME)
    logger.setLevel(logging.INFO)
    log_dir_path = os.path.join(BASE_PATH, 'logs')
    log_path = os.path.join(log_dir_path, 'app.log')
    # 使用 TimedRotatingFileHandler 按天切割日志
    file_handler = TimedRotatingFileHandler(
        log_path,
        when='midnight',  # 每天午夜切割日志
        interval=1,  # 间隔单位（天）
        backupCount=5,  # 保留 5 个备份文件
        encoding='utf-8'  # 如果需要支持中文，可以指定编码
    )
    file_handler.setLevel(logging.INFO)

    # 创建日志格式器并定义日志格式
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    return logger
