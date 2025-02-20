import os
# 邮箱参数
MAIL_HOST = "Exchange.1bizmail.com"  # 设置服务器
MAIL_USER = "it-21@1bizmail.com"  # 用户名
MAIL_PASSWD = "Abcd1234"  # 口令
MAIL_FROM = "DevOopsPlatform"  # 发件人

# 日志参数
# 日志名称
LOG_NAME = 'devops'
# 日志格式：日期 - 日志名称 - 等级 - 函数名 - 信息
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s  - %(message)s "
# 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))