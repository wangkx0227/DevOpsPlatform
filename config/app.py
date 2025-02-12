from flask import Flask
from flask_restful import Resource, Api

app = Flask(__file__)  # app 对象
api = Api(app)  # api 对象
