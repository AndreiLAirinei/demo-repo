from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from datetime import datetime
import json

app = Flask("TodolistAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('dueDate', type=datetime, required=False, location='form')


with open('tasks.json', 'r') as f:
    tasks = json.load(f)


def write_changes_to_file():
    global tasks
    # This sorts the tasks after a criteria, in this care being the value of the dictionary, 'name'
    tasks = {k: v for k, v in sorted(tasks.items(), key=lambda tasks: tasks[1]['name'])}
    # Creates a file 'tasks' if one is not found in the folder
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)


class Task(Resource):

    @staticmethod
    def get(task_id):
        if task_id == "all":
            return tasks
        if task_id not in tasks:
            abort(404, message=f'Task {task_id} was not found!')
        return tasks[task_id]

    @staticmethod
    def put(task_id):
        args = parser.parse_args()
        new_task = {'name': args['name'],
                    'dueDate': args['dueDate']}

        if new_task.items[2] == None:
            new_task['dueDate'] = datetime.today().year

        tasks[task_id] = new_task
        write_changes_to_file()
        return {task_id: tasks[task_id]}, 201

    @staticmethod
    def delete(task_id):
        if task_id not in tasks:
            abort(404, message=f'Task {task_id} was not found!')
        del tasks[task_id]
        write_changes_to_file()
        return "", 204


class TaskSchedule(Resource):
    # This class creates a task without being provided an id
    @staticmethod
    def post():
        args = parser.parse_args()
        new_task = {'name': args['name'],
                    'dueDate': args['dueDate']}
        task_id = max(int(v.lstrip('task')) for v in tasks.keys()) + 1
        # Takes all the task ids, stripping the 'task', converting it to
        # an integer then making a list and adding 1
        task_id = f"task{task_id}"

        if not new_task['dueDate']:
            new_task['dueDate'] = datetime.today().year

        tasks[task_id] = new_task
        write_changes_to_file()
        return tasks[task_id], 201


api.add_resource(Task, '/tasks/<task_id>')
api.add_resource(TaskSchedule, '/tasks')

if __name__ == '__main__':
    app.run()

