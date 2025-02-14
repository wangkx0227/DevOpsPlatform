from flask import jsonify
from devops_app.utilits import logger



class ApiResponse:
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
        return jsonify(response_data), self.status

    @staticmethod
    def success(data=None, message="Success", status=200):
        """
        成功响应，记录日志。
        """
        logger.info(f"Response: status={status}, message={message}")
        return ApiResponse(data=data, status=status, message=message).to_response()

    @staticmethod
    def error(data=None, message="Error", status=400):
        """
        错误响应，记录日志。
        """
        logger.error(f"Response: status={status}, message={message}")
        return ApiResponse(data=data, status=status, message=message).to_response()
