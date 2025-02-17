# 检测
from flask import Blueprint
from flask_restful import Api

detection_bp = Blueprint('bp', __name__)  # 蓝图
detection_api = Api(detection_bp)  # api

from . import routes

__all__ = [
    "detection_bp"
]
