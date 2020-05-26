import os

from flask import Flask
from flask_restful import Api

from controllers import setup_controllers
from resources.smoke import SmokeResource


def create_app():
    config_path = os.path.abspath(os.path.join('config/config.json', ))

    app = Flask(__name__)
    app.config.from_json(config_path)
    setup_controllers(app)

    return app


def register_api(app):
    from api import projects, materials, articles
    api = Api(app)
    api.add_resource(SmokeResource, "/smoke")
    app.register_blueprint(projects)
    app.register_blueprint(materials)
    app.register_blueprint(articles)


app = create_app()
register_api(app)
