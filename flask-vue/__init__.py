import os
from flask import Flask
from flask_restplus import Api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='my-secret-key'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import flask_vue
    app.register_blueprint(flask_vue.bp)
    from .rest_api import api as ns_rest
    # register API
    api = Api(app,
              version='0.1',
              title='Flask-Vue',
              description='A simple Flask-vue and mongodb example',
              # doc describes the route to the swagger documentation
              doc='/doc/')
    api.add_namespace(ns_rest)

    return app
