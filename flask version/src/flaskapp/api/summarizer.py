from flask import request
from flask_restful import Resource, reqparse, abort

from ..model import get_summary


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('text',  type=str, required=True)
parser.add_argument('max_length',  type=int, required=True)


class Summarizer(Resource):

    def post(self):
        args = parser.parse_args(strict=True)
        long_text = args['text']
        max_length = args['max_length']

        if long_text is None or max_length is None:
            abort(404, message='Text or max_length is not available')

        max_length = int(max_length)
        summary_text = get_summary(long_text=long_text, max_length=max_length)

        return {'summary_text': summary_text}, 200
