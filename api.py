from flask import Blueprint
from flask_restful import Api

from resources.project import ProjectViewResource, ProjectsResource

projects = Blueprint("projects", __name__, url_prefix="/projects")
api_projects = Api(projects)
api_projects.add_resource(ProjectsResource, "")
api_projects.add_resource(ProjectViewResource, "/<int:project_id>")

materials = Blueprint("materials", __name__, url_prefix="/materials")
articles = Blueprint("articles", __name__, url_prefix="/articles")


