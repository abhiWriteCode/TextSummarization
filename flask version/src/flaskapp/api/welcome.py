from flask import request
from flask_restful import Resource


class Welcome(Resource):

    def get(self):
        return {'message': 'Welcome To TextSummarization.com'}, 200
