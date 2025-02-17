import os

# 端口
POST = "8080"
# 主机ip
HOST = "0.0.0.0"
# 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 日志名称
LOG_NAME = 'devops'
# 日志格式：日期 - 日志名称 - 等级 - 函数名 - 信息
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s  - %(message)s "
