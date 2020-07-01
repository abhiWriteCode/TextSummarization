from flask import Blueprint
from flask_restful import Api

from .summarizer import Summarizer
from .welcome import Welcome


def add_resources(app):
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(Welcome, '/')
    api.add_resource(Summarizer, '/summary')

    app.register_blueprint(api_bp)

    return app
