from flask_restful import Resource, marshal_with

from controllers.project import create
from shemas.project import ext_project_schema, project_list_schema, post_project_parser
from utils.resource_utils import make_response


class ProjectsResource(Resource):

    @marshal_with(project_list_schema)
    def get(self):
        return "projects", 200

    @marshal_with(ext_project_schema)
    def post(self):
        """
        Add new project with "Blueprint" status"
        :param request:
        :return:
        """
        args = post_project_parser.parse_args()

        result = create(args)
        return make_response(result)


class ProjectViewResource(Resource):
    @marshal_with(ext_project_schema)
    def get(self, id_):
        return f"project view {id_}", 200

    @marshal_with(ext_project_schema)
    def put(self, id_):
        pass

    @marshal_with(ext_project_schema)
    def delete(self, id_):
        pass
