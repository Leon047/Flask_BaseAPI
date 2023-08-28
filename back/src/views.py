from flask_restful import Resource

# from .models import ExampleModel
# from .schemas import ExampleSchema


class HelloWorld(Resource):

    def get(self):
        return {'data': 'Hello World'}, 200
