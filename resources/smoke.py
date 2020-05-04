from flask_restful import Resource


class SmokeResource(Resource):
    def get(self):
        return "Hi", 200
