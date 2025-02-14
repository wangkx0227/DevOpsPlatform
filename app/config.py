from flask import Flask
from flask_restful import Resource, Api


class DefaultConfig:  # 生产模式 所需要的全部参数
    SECRET_KEY = ''


class DevelopmentConfig(DefaultConfig):  # 调试模式下的参数
    '''继承了生成模式的类'''
    DEBUG = True


def create_app(config_filename):
    app = Flask(__file__)  # app 对象
    api = Api(app)  # api 对象
    return
