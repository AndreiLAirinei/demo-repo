from flask import Flask
from flask_restful import Api
from TaskController import Controller
from Repository import InMemoryRepository


app = Flask("main")
api = Api(app)

repository = InMemoryRepository()

# Route for all tasks (GET, POST)
api.add_resource(Controller, '/tasks',
                 endpoint='tasks_all',
                 resource_class_kwargs={'repository': repository})

# Route for a specific task by ID (GET, PUT, PATCH, DELETE)
api.add_resource(Controller, '/tasks/<string:task_id>',
                 endpoint='tasks_by_id',
                 resource_class_kwargs={'repository': repository})


if __name__ == '__main__':
    app.run(debug=True)
