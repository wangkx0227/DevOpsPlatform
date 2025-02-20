import os
from flask import Flask

from core.blueprints import detection_bp

# 项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app(config_filename):
    app = Flask(__file__)  # app 对象
    app.config.from_object(config_filename)
    app.register_blueprint(detection_bp, url_prefix='/api')

    # 静态文件创建
    static_dir_path = os.path.join(BASE_PATH, "static")
    if not os.path.exists(static_dir_path):
        os.mkdir(static_dir_path)
    # 文件
    files_dir_path = os.path.join(static_dir_path, "files")
    if not os.path.exists(files_dir_path):
        os.mkdir(files_dir_path)
    # 图片
    pictures_dir_path = os.path.join(static_dir_path, "pictures")
    if not os.path.exists(pictures_dir_path):
        os.mkdir(pictures_dir_path)
    return app
