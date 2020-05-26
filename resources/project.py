from flask_restful import Resource, marshal_with

from app import app
from shemas.project import ext_project_schema, project_list_schema, post_project_parser, get_project_parser
from utils.resource_utils import make_response


class ProjectsResource(Resource):

    @marshal_with(project_list_schema)
    def get(self):
        """Get list of projects that match parsed request args
        :return:
            dict: {"status": success or failure, "message": error message if error, "data": List of projects}
        """

        args = get_project_parser.parse_args()

        controller = app.controllers.ProjectController
        result, status = controller.get_projects(args)
        return make_response(result), status

    @marshal_with(ext_project_schema)
    def post(self):
        """Add new project with "Blueprint" status"
        :return:
            dict: {"status": success or failure, "message": error message if error, "data": created project dict}
        """

        args = post_project_parser.parse_args()

        controller = app.controllers.ProjectController
        result, status = controller.create_project(args)
        return make_response(result), status


class ProjectViewResource(Resource):
    @marshal_with(ext_project_schema)
    def get(self, project_id):
        """Get project by id
        :param: project_id: id for project filtering
        :return:
            dict: {"status": success or failure, "message": error message if error, "data": project dict}
        """

        args = {"id": project_id}

        controller = app.controllers.ProjectController
        result, status = controller.get_project(args)
        return make_response(result), status

    @marshal_with(ext_project_schema)
    def put(self, project_id):
        """Update project by id with parsed request args
        :return:
            dict: {"status": success or failure, "message": error message if error, "data": project dict}
        """

        args = get_project_parser.parse_args()
        args["id"] = project_id

        controller = app.controllers.ProjectController
        result, status = controller.update_project(args)
        return make_response(result), status

    @marshal_with(ext_project_schema)
    def delete(self, project_id):
        """Delete project by id
        :return:
            dict: {"status": success or failure, "message": error message if error, "data": empty dict}
        """

        args = {"id": project_id}

        controller = app.controllers.ProjectController
        result, status = controller.delete_project(args)
        return make_response(result), status
