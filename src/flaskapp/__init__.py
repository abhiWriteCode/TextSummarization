import os
from flask import Flask


def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=False)

	app.config.from_mapping(
		SECRET_KEY='secret',
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=False)
	else:
		app.config.from_mapping(test_config)

	# try:
	# 	os.makedirs(app.instance_path)
	# except OSError:
	# 	pass

	from .api import add_resources
	app = add_resources(app)

	return app
	