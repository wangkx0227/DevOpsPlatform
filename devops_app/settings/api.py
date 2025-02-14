from flask_restful import Resource


class ApiBase(Resource):
    """
        api 父类
    """

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass
