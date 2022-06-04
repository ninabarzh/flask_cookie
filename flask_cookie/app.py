from flask_cookie.ext import api, configuration, database
from flask_cookie.models.news import News  # pylint: disable=W0611
from flask_cookie.models.users import User  # pylint: disable=W0611


def create_app(**config):
    """Cria flask app"""
    app = api.create_api_app()
    configuration.init_app(app, **config)
    database.init_app(app)
    return app
