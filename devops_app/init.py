from flask import Flask
from .blueprints.detection import detection_bp


def create_app(config_filename):
    app = Flask(__file__)  # app 对象
    app.config.from_object(config_filename)
    app.register_blueprint(detection_bp, url_prefix='/api')

    return app



