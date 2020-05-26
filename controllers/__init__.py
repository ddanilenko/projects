from collections import namedtuple


def setup_controllers(app):
    from controllers.project import ProjectController

    controllers = namedtuple(
        'controllers',
        ['ProjectController']
    )
    app.controllers = controllers(
        ProjectController()
    )
