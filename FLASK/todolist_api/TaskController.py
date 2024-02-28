from flask.views import MethodView
from flask_restful import abort, reqparse
from datetime import datetime


def parser():
    parser_args = reqparse.RequestParser()

    parser_args.add_argument('name', type=str, required=True)
    parser_args.add_argument('assigner', type=str, required=True)
    parser_args.add_argument('company', type=str, required=True)

    parser_args.add_argument('deadline', type=str)
    parser_args.add_argument('priority', type=int)
    parser_args.add_argument('description', type=str)
    parser_args.add_argument('status', default='In progress')
    parser_args.add_argument('assigned_personnel', type=str)
    parser_args.add_argument('creation_date', type=datetime,
                             default=datetime.today())
    parser_args.add_argument('last_modified_date', type=datetime,
                             default=datetime.today())
    parser_args.add_argument('comments', type=str)

    args = parser_args.parse_args()

    if not args['name'] or not args['assigner'] or not args['company']:
        abort(400, message="Bad request: Missing or incorrect data in the request.")
    return args


def parser_create():
    args = parser()

    creation_date = args['creation_date'].strftime('%Y-%m-%d %H:%M')
    last_modified_date = args['last_modified_date'].strftime('%Y-%m-%d %H:%M')

    new_data = {
        "name": args["name"],
        "assigner": args['assigner'],
        "company": args['company'],
        "deadline": args['deadline'],
        "priority": args['priority'],
        "description": args['description'],
        "status": args['status'],
        "assigned_personnel": args['assigned_personnel'],
        "creation_date": creation_date,
        "last_modified_date": last_modified_date,
        "comments": args['comments'],
    }

    return new_data


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
        new_data = parser_create()
        self.repository.create(new_data)
        abort(200, message=f"Task created successfully!")

    def put(self, task_id):
        if self.repository.task_exists(task_id):
            existing_task = self.repository.get_by_id(task_id)

            existing_task['last_modified_date'] = datetime.today().strftime('%Y-%m-%d %H:%M')
            updated_data = parser_create()

            self.repository.update(task_id, updated_data)
            return abort(200, message=f"Task created successfully!")
        else:
            abort(404, message=f"Task {task_id} was not found!")

    def patch(self, task_id, updated_data):
        if self.repository.task_exists(task_id):

            # Get the existing task from the repo
            existing_task = self.repository.get_by_id(task_id)

            # Adjusting and formatting last modified date to %Y-%m-%d format
            existing_task['last_modified_date'] = datetime.today().strftime('%Y-%m-%d %H:%M')

            for field, value in updated_data.items():
                if field in existing_task:
                    existing_task[field] = value
                else:
                    abort(404, message=f"Field '{field}' not found in task with ID {task_id}.")

            self.repository.update(task_id, existing_task)
            return abort(200, message=f"Task with ID {task_id} patched successfully.")
        else:
            abort(404, message=f"Task with ID {task_id} not found.")

    def delete(self, task_id):
        if self.repository.task_exists(task_id):
            self.repository.delete(task_id)
            return abort(200, message=f"Task with ID {task_id} deleted successfully.")
        else:
            abort(404, message=f'Task {task_id} was not found!')
