from flask import Flask
from flask_restful import Api

from api import projects, materials, articles
from config import Config
from resources.smoke import SmokeResource

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


api.add_resource(SmokeResource, "/smoke")
app.register_blueprint(projects)
app.register_blueprint(materials)
app.register_blueprint(articles)

