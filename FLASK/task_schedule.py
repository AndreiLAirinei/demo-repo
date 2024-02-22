from flask_restful import Resource
from todo_list_file_changes import write_changes_to_file, tasks
from task import parser


class TaskSchedule(Resource):
    # This class creates a task without being provided an id

    @classmethod
    def get(cls):
        return tasks

    @classmethod
    def post(cls):
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
