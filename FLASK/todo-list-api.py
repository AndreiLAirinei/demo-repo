from flask import Flask
from flask_restful import Api
from task import Task
from task_schedule import TaskSchedule


app = Flask("TodolistAPI")
api = Api(app)


api.add_resource(Task, '/tasks/<task_id>')
api.add_resource(TaskSchedule, '/tasks')

if __name__ == '__main__':
    app.run()
