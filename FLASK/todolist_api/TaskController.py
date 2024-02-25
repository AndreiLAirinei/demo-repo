from flask.views import MethodView


# Interface
class Controller(MethodView):
    def __init__(self, repository):
        self.repository = repository

    def get(self, task_id):
        if task_id is None or task_id.lower() == "all":
            return self.repository.get_all()
        else:
            return self.repository.get_by_id(task_id)

    def post(self):
        return self.repository.post()

    def put(self, item_id, data):
        pass

    def patch(self, item_id, data):
        pass

    def delete(self, item_id):
        pass


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