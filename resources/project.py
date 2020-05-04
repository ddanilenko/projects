from flask_restful import Resource


class ProjectsResource(Resource):
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class ProjectsCollectionResource(Resource):
    def get(self):
        return "projects", 200


class ProjectViewResource(Resource):
    def get(self, id_):
        return f"project view {id_}", 200
