import json
import uuid
from datetime import datetime

from flask import Response, request
from flask_restful import Resource

from core.utilits import logger


class BaseConfig:
    __doc__ = "配置父类"
    SECRET_KEY = str(uuid.uuid4())  # 随机密钥
    START_TIME = datetime.now()


class DefaultConfig(BaseConfig):  # 生产模式 所需要的全部参数
    __doc__ = "生产类"
    pass


class DevelopmentConfig(BaseConfig):  # 调试模式下的参数
    __doc__ = "调试类"
    DEBUG = True


class ApiBase(Resource):
    __doc__ = "API父类"

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass


class ApiResponse:
    __doc__ = "响应类"

    def __init__(self, data=None, status=200, message=""):
        self.data = data
        self.status = status
        self.message = message

    def to_response(self):
        """
        将响应数据转换为 Flask 的 Response 对象
        """
        response_data = {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }
        response = Response(json.dumps(response_data), mimetype='application/json', status=self.status)
        return response

    @staticmethod
    def success(data=None, message="Success", status=200):
        """
        成功响应，记录日志。
        """
        request_info = f"{request.method} - {status} - {request.path} - {request.url} - {request.remote_addr}"
        logger.info(f"{message} - {request_info}")
        return ApiResponse(data=data, status=status, message=message).to_response()

    @staticmethod
    def error(data=None, message="Error", status=400):
        """
        错误响应，记录日志。
        """
        request_info = f"{request.method} - {status} - {request.path} - {request.url} - {request.remote_addr}"
        logger.error(f"{message} - {request_info}")
        return ApiResponse(data=data, status=status, message=message).to_response()
