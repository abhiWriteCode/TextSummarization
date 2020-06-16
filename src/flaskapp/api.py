from flask import request
from flask_restful import Resource, abort

from .model import get_summary


class Welcome(Resource):

	def get(self):
		return {'message': 'Welcome To TextSummarization.com'}, 200


class Summarizer(Resource):

	def post(self):
		long_text = request.form.get('text', None)
		max_length = request.form.get('max_length', None)

		if long_text is None or max_length is None:
			abort(404, message='Text or max_length is not available')

		max_length = int(max_length)
		summary_text = get_summary(long_text=long_text, max_length=max_length)

		return {'summary_text': summary_text}, 200