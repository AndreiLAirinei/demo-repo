from TaskController import Controller
from file_changes import read_tasks_from_file as tasks, write_changes_to_file
from flask_restful import abort, reqparse


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, location='form')
parser.add_argument('assigner', type=str, required=True, location='form')
parser.add_argument('company', type=str, required=True, location='form')
parser.add_argument('deadline', type=str, required=False, location='form')
parser.add_argument('priority', type=int, required=False, location='form')
parser.add_argument('description', type=str, required=False, location='form')
parser.add_argument('status', type=str, required=False, location='form')
parser.add_argument('assigned_personnel', type=str, required=False, location='form')
parser.add_argument('creation_date', type=str, required=False, location='form')
parser.add_argument('last_modified_date', type=str, required=False, location='form')
parser.add_argument('comments', type=str, required=False, location='form')


class InMemoryRepository(Controller):
    """ A repository class that stores tasks in memory. """
    def __init__(self):
        """
        Initializes the InMemoryRepository by reading tasks from a file.
        If there's an error reading tasks from the file, it raises an error.
        """
        try:
            self.__data = tasks()
        except Exception as error:
            print(f"Error loading tasks from file: {error}")

    def get_all(self):
        return self.__data

    def get_by_id(self, task_id):
        if task_id is None or task_id.lower() == "tasks_all":
            return self.__data
        elif task_id not in tasks():
            abort(404, message=f'Task {task_id} was not found!')
        else:
            task_data = self.__data[task_id].copy()  # Create a copy to avoid modifying the original data
            return task_data

    def post(self):
        args = parser.parse_args()
        task_id = self.generate_task_id()

        # Creating a new task using the parsed arguments
        new_task = {
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
        new_task = {task_id: new_task}

        self.__data[task_id] = new_task
        write_changes_to_file(new_task)
        return new_task

    def generate_task_id(self):
        existing_tasks = self.__data

        if not existing_tasks:
            new_task_id = "task1"
        else:
            existing_id = [int(v.lstrip('task')) for v in existing_tasks.keys()]
            new_task_id = f"task{max(existing_id) + 1}"
            print(existing_id)

        return new_task_id

