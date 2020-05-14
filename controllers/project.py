from database import session
from models import Project, ProjectType, User
from utils.db_utils import create, base


@base
@create
def create(args):
    associations = [
        {"association": "project_types", "model": ProjectType, "associated_list": args.pop("project_types", [])},
        {"association": "responsible", "model": User, "associated_list": args.pop("responsible", [])},
        {"association": "project_votes", "model": User, "associated_list": args.pop("project_votes", [])}
    ]

    project = Project(**args)
    for av in associations:
        associated_values = session.query(av["model"]).filter(
            av["model"].id.in_(av["associated_list"])).all()
        project.add_associates(av["association"], associated_values)

    return project
