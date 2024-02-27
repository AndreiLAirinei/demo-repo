from flask.views import MethodView
from flask_restful import abort, reqparse


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, location='form')
parser.add_argument('assigner', type=str, required=True, location='form')
parser.add_argument('company', type=str, required=True, location='form')
parser.add_argument('deadline', type=str, location='form')
parser.add_argument('priority', type=int, location='form')
parser.add_argument('description', type=str, location='form')
parser.add_argument('status', type=str, location='form')  # automat
parser.add_argument('assigned_personnel', type=str, location='form')
parser.add_argument('creation_date', type=str, location='form')  # automat
parser.add_argument('last_modified_date', type=str, location='form')  # automat
parser.add_argument('comments', type=str, location='form')


# Interface
class Controller(MethodView):
    def __init__(self, repository):
        self.repository = repository

    def get(self, task_id):
        if task_id.lower() == "all":
            return self.repository.get_all()
        elif self.repository.task_exists(task_id):
            return self.repository.get_by_id(task_id)
        else:
            abort(404, message=f'Task {task_id} was not found!')

    def post(self):
        args = parser.parse_args()

        # Creating a new task using the parsed arguments
        new_data = {
            "name": args["name"],
            "assigner": args['assigner'],
            "company": args['company'],
            "deadline": args['deadline'],
            "priority": args['priority'],
            "description": args['description'],
            "status": args['status'],
            "assigned_personnel": args['assigned_personnel'],
            "creation_date": args['creation_date'],
            "last_modified_date": args['last_modified_date'],
            "comments": args['comments'],
        }

        return self.repository.create(new_data)

    def put(self, task_id, data):
        pass

    def patch(self, task_id, data):
        pass

    def delete(self, task_id):
        if self.repository.task_id.task_exists(task_id):
            return self.repository.delete(task_id), 204
        else:
            abort(404, message=f'Task {task_id} was not found!')


"""
    def put(cls, task_id):
        args = parser.parse_args()
        new_task = {'name': args['name'],
                    'dueDate': args['dueDate']}

        if not new_task['dueDate']:
            new_task['dueDate'] = datetime.today().year

        tasks[task_id] = new_task
        write_changes_to_file()
        return {task_id: tasks[task_id]}, 201


    def delete(cls, task_id):
        if task_id not in tasks:
            abort(404, message=f'Task {task_id} was not found!')
        del tasks[task_id]
        write_changes_to_file()
        return "", 204
"""