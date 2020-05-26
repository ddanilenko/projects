from database import session
from models import Project, ProjectType, User
from utils.db_utils import base, create, get, delete, update
from werkzeug.exceptions import NotFound


class ProjectController:
    model = Project

    @base
    @get
    def get_projects(self, args):
        projects = session.query(self.model).filter_by(**args).all()
        return projects

    @base
    @get
    def get_project(self, args):
        project = session.query(self.model).filter_by(**args).first()
        if not project:
            raise NotFound(description=f'There is no project with {args["id"]} id')
        return project

    @base
    @create
    def create_project(self, args):
        associations = [
            {"association": "project_types", "model": ProjectType, "associated_list": args.pop("project_types", [])},
            {"association": "responsible", "model": User, "associated_list": args.pop("responsible", [])},
            {"association": "project_votes", "model": User, "associated_list": args.pop("project_votes", [])}
        ]
        args["status_title"] = "Blueprint"
        project = self.model(**args)
        for av in associations:
            associated_values = session.query(av["model"]).filter(
                av["model"].id.in_(av["associated_list"])).all()
            project.add_associates(av["association"], associated_values)

        return project

    @base
    @update
    def update_project(self, args):
        pass

    @base
    @delete
    def delete_project(self, args):
        project = session.query(self.model).filter_by(**args).first()
        return project
