from . import detection_api

from .views import DetectionApi

detection_api.add_resource(DetectionApi, '/healthcheck')