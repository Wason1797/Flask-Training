from flask import Flask
from .service import urls
from .plugins import db, ma


def create_app(config_class):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    __register_plugins(flask_app)

    return flask_app


def __register_plugins(flask_app):
    flask_app.register_blueprint(urls, url_prefix='/api')
    db.init_app(flask_app)
    ma.init_app(flask_app)
