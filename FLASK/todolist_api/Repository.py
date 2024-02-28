from file_changes import write_changes_to_file, read_tasks_from_file


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
        return self.__data  # Returns all the data in the repository

    def get_by_id(self, task_id):
        task_data = self.__data[task_id].copy()  # Create a copy to avoid modifying the original data
        return task_data  # Returns the data

    def create(self, attr):
        task_id = self.generate_task_id()  # Generates ID
        new_task = {task_id: attr}  # Creates the new task

        self.__data[task_id] = new_task  # Adds the new task to the data
        write_changes_to_file(new_task)  # Writes the updated data back to file
        return new_task  # Returns the newly created task

    def update(self, task_id, attr):

        updated_task = {task_id: attr}
        self.__data = updated_task
        write_changes_to_file(updated_task)
        return updated_task

    def delete(self, task_id):
        deleted_task = self.__data.pop(task_id)  # Removes the item and returns its value
        write_changes_to_file(self.__data)  # Writes the updated data back to file
        return deleted_task  # Returns the deleted task (for double-checking)

    #  Checks if a tasks exists or not.
    @staticmethod
    def task_exists(task_id):
        if task_id not in read_tasks_from_file():
            print(f"Task with ID {task_id} does not exist.")
            return False
        return True

    # Generates an ID for each created task
    def generate_task_id(self):
        existing_tasks = self.__data

        if not existing_tasks:
            new_task_id = "task1"
        else:
            existing_id = [int(v.lstrip('task')) for v in existing_tasks.keys()]
            new_task_id = f"task{max(existing_id) + 1}"

        return new_task_id
