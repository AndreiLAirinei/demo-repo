from flask.views import MethodView
from flask_restful import abort, reqparse

from task import Task
from datetime import datetime

from exceptions import TaskNotFoundError, InvalidTaskIdError, ParsingError


def parser():
    parser_args = reqparse.RequestParser()

    parser_args.add_argument('name', type=str, required=True)
    parser_args.add_argument('assigner', type=str, required=True)
    parser_args.add_argument('company', type=str, required=True)

    parser_args.add_argument('deadline', type=lambda
        x: datetime.strptime(x, '%Y-%m-%d %H:%M') if x else None)
    parser_args.add_argument('priority', type=int)
    parser_args.add_argument('description', type=str)
    parser_args.add_argument('assigned_personnel', type=str)
    parser_args.add_argument('comments', type=str)

    try:
        args = parser_args.parse_args()
        if not args['name'] or not args['assigner'] or not args['company']:
            raise ParsingError()
        return args
    except ParsingError as error:
        abort(error.status_code, message=str(error))


def parser_create():
    args = parser()

    new_data = {
        "name": args["name"],
        "assigner": args['assigner'],
        "company": args['company'],
        "deadline": args['deadline'],
        "status": Task().status,
        "priority": args['priority'],
        "description": args['description'],
        "assigned_personnel": args['assigned_personnel'],
        "creation_date": Task().creation_date,
        "last_modified_date": Task().last_modified_date,
        "comments": args['comments'],
    }

    return new_data


# Interface
class Controller(MethodView):
    def __init__(self, repository):
        self.repository = repository

    def get(self, task_id):
        try:
            if task_id.lower() == "all":
                return self.repository.get_all()

            if not self.repository.is_valid_task_id(task_id):
                raise InvalidTaskIdError(task_id)

            elif self.repository.task_exists(task_id):
                return self.repository.get_by_id(task_id)
            else:
                raise TaskNotFoundError(task_id)

        except (InvalidTaskIdError, TaskNotFoundError) as error:
            status_code = 404 if isinstance(error, TaskNotFoundError) else 400
            abort(status_code, message=str(error))

    def post(self):
        new_data = parser_create()
        self.repository.create(new_data)
        return {"message": f"Task created successfully."}, 200

    def put(self, task_id):
        if self.repository.task_exists(task_id):
            existing_task = self.repository.get_by_id(task_id)

            existing_task['last_modified_date'] = datetime.today().strftime('%Y-%m-%d %H:%M')
            updated_data = parser_create()

            self.repository.update(task_id, updated_data)
            return {"message": f"Task with ID {task_id} created successfully."}, 200
        else:
            abort(404, message=f"Task {task_id} was not found!")

    def patch(self, task_id, updated_field):
        if self.repository.task_exists(task_id):

            # Get the existing task from the repo
            existing_task = self.repository.get_by_id(task_id)

            # Adjusting and formatting last modified date to %Y-%m-%d format
            existing_task['last_modified_date'] = datetime.today().strftime('%Y-%m-%d %H:%M')

            for field, value in updated_field.items():
                if field in existing_task:
                    existing_task[field] = value
                else:
                    abort(404, message=f"Field '{field}' not found in task with ID {task_id}.")

            self.repository.update(task_id, existing_task)
            return {"message": f"Task with ID {task_id} patched successfully."}, 200
        else:
            abort(404, message=f"Task with ID {task_id} not found.")

    def delete(self, task_id):
        if self.repository.task_exists(task_id):
            self.repository.delete(task_id)
            return {"message": f"Task with ID {task_id} deleted successfully."}, 200
        else:
            abort(404, message=f'Task {task_id} was not found!')

    def update_status_to_done(self, task_id):
        if self.repository.task_exists(task_id):
            task = self.repository.get_by_id(task_id)
            task['status'] = "Done"

            self.repository.update(task_id, task)

            return {"message": f"Task's status with ID {task_id} updated successfully."}, 200
        else:
            abort(404, message=f"Task {task_id} was not found!")
