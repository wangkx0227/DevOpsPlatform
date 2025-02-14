# 检测
from flask import  Blueprint
from flask_restful import Api

detection_bp = Blueprint('bp', __name__)
detection_api = Api(detection_bp)

from . import routes

