from file_changes import write_changes_to_file, read_tasks_from_file
import re

class JSONRepository:
    """ A repository class that stores tasks in memory. """
    def __init__(self):
        """
        Initializes the InMemoryRepository by reading tasks from a file.
        If there's an error reading tasks from the file, it raises an error.
        """
        try:
            self.__data = read_tasks_from_file()
        except Exception as error:
            print(f"Error loading tasks from file: {error}")

    def get_all(self):
        return self.__data

    def get_by_id(self, task_id):
        task_data = self.__data[task_id].copy()  # Create a copy to avoid modifying the original data
        return task_data  # Returns the data

    def create(self, attr):
        task_id = self.generate_task_id()
        new_task = {task_id: attr}

        self.__data[task_id] = new_task
        write_changes_to_file(new_task)
        return new_task

    def update(self, task_id, updated_data):
        updated_task = {task_id: updated_data}
        self.__data = updated_task
        write_changes_to_file(updated_task)
        return updated_task

    def patch(self, task_id, updated_task):
        self.__data[task_id] = updated_task
        write_changes_to_file(self.__data)
        return updated_task

    def delete(self, task_id):
        deleted_task = self.__data.pop(task_id)
        write_changes_to_file(self.__data)
        return deleted_task

    def task_exists(self, task_id):
        if task_id not in self.__data:
            return False
        return True

    @staticmethod
    def is_valid_task_id(task_id):
        pattern = re.compile(r'^task\d+$')
        return bool(pattern.match(task_id))

    def generate_task_id(self):
        existing_tasks = self.__data

        if not existing_tasks:
            new_task_id = "task1"
        else:
            existing_id = [int(v.lstrip('task')) for v in existing_tasks.keys()]
            new_task_id = f"task{max(existing_id) + 1}"

        return new_task_id
