from flask_restful import Resource, reqparse, abort
from todo_list_file_changes import write_changes_to_file, tasks
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('dueDate', type=datetime, required=False, location='form')


class Task(Resource):

    @classmethod
    def get(cls, task_id):
        if task_id == "all":
            return tasks
        if task_id not in tasks:
            abort(404, message=f'Task {task_id} was not found!')
        return tasks[task_id]

    @classmethod
    def put(cls, task_id):
        args = parser.parse_args()
        new_task = {'name': args['name'],
                    'dueDate': args['dueDate']}

    #    if new_task.items[2] is None:
    #        new_task['dueDate'] = datetime.today().year

        tasks[task_id] = new_task
        write_changes_to_file()
        return {task_id: tasks[task_id]}, 201

    @classmethod
    def delete(cls, task_id):
        if task_id not in tasks:
            abort(404, message=f'Task {task_id} was not found!')
        del tasks[task_id]
        write_changes_to_file()
        return "", 204
