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
    return args


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
        if parser():
            args = parser()

            # Converting the creation date & last modified date to %Y-%m-%d format
            creation_date = args['creation_date'].strftime('%Y-%m-%d %H:%M')
            last_modified_date = args['last_modified_date'].strftime('%Y-%m-%d %H:%M')

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
                "creation_date": creation_date,
                "last_modified_date": last_modified_date,
                "comments": args['comments'],
            }
            return self.repository.create(new_data)
        else:
            return f"Missing parsed attributes. ", 500

    def put(self, task_id):
        if self.repository.task_exists(task_id):
            if parser():
                args = parser()

                # Adjusting and formatting last modified date to %Y-%m-%d format
                args['last_modified_date'] = datetime.today()
                last_modified_date = args['last_modified_date'].strftime('%Y-%m-%d %H:%M')

                # Get the existing task from the repo to retain its creation_date
                existing_task = self.repository.get_by_id(task_id)

                # Updating the task using the parsed arguments
                updated_data = {
                    "name": args["name"],
                    "assigner": args['assigner'],
                    "company": args['company'],
                    "deadline": args['deadline'],
                    "priority": args['priority'],
                    "description": args['description'],
                    "status": args['status'],
                    "assigned_personnel": args['assigned_personnel'],
                    "creation_date": existing_task['creation_date'],
                    "last_modified_date": last_modified_date,
                    "comments": args['comments'],
                }

                self.repository.update(task_id, updated_data)

                return f"Task with ID {task_id} updated successfully.", 200
            else:
                return f"Missing parsed attributes.", 400
        else:
            abort(404, message=f'Task {task_id} was not found!')

    def patch(self, task_id, updated_field):
        if self.repository.task_exists(task_id):
            if parser():
                args = parser()
                # Get the existing task from the repo
                existing_task = self.repository.get_by_id(task_id)

                # Adjusting and formatting last modified date to %Y-%m-%d format
                args['last_modified_date'] = datetime.today()
                last_modified_date = args['last_modified_date'].strftime('%Y-%m-%d %H:%M')

                # Checks if the fields is in the task
                if updated_field in existing_task[task_id]:
                    # Updates said field
                    existing_task[task_id][updated_field] = args[updated_field]
                    existing_task[task_id]['last_modified_date'] = last_modified_date

                    print(f"Task with ID {task_id} updated successfully."), 200

                    return self.repository.patch(task_id, existing_task[task_id])
                else:
                    # Field not found, return appropriate status code and message
                    abort(404, message=f"Field '{updated_field}' not found in task with ID {task_id}.")
            else:
                # Missing parsed attributes, return appropriate status code and message
                abort(400, message="Missing parsed attributes.")
        else:
            # Task not found, return appropriate status code and message
            abort(404, message=f"Task with ID {task_id} not found.")

    def delete(self, task_id):
        if self.repository.task_exists(task_id):
            return self.repository.delete(task_id)
        else:
            abort(404, message=f'Task {task_id} was not found!')
