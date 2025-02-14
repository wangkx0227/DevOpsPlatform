import uuid
from datetime import datetime

class BaseConfig:
    SECRET_KEY = str(uuid.uuid4())  # 随机密钥
    START_TIME = datetime.now()



class DefaultConfig(BaseConfig):  # 生产模式 所需要的全部参数
    """
        生产类
    """
    pass


class DevelopmentConfig(BaseConfig):  # 调试模式下的参数
    """
        调试类
    """
    DEBUG = True
