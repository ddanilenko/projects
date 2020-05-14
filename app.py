import os
from flask import Flask
from flask_restful import Api

from api import projects, materials, articles
from resources.smoke import SmokeResource


config_path = os.path.abspath(os.path.join('config/config.json', ))

app = Flask(__name__)
app.config.from_json(config_path)
api = Api(app)


api.add_resource(SmokeResource, "/smoke")
app.register_blueprint(projects)
app.register_blueprint(materials)
app.register_blueprint(articles)

