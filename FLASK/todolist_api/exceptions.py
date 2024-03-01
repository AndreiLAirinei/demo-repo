
class FileError(Exception):
    def __init__(self, message="File-related error"):
        super().__init__(message)


class FileNotFoundError(Exception):
    def __init__(self, message="File not found"):
        super().__init__(message)


class JSONDecodeError(Exception):
    def __init__(self, message="Error decoding JSON"):
        super().__init__(message)


class TaskNotFoundError(Exception):
    def __init__(self, task_id, message="Task does not exist"):
        super().__init__(message)
        self.task_id = task_id
        self.message = message

    def __str__(self):
        return f"{self.message} (Task ID: {self.task_id})"


class InvalidTaskIdError(Exception):
    def __init__(self, task_id, message="Invalid task ID"):
        super().__init__(message)
        self.task_id = task_id
        self.message = message

    def __str__(self):
        return f"{self.message} (Task ID: {self.task_id})"


class ParsingError(Exception):
    def __init__(self, message=""):
        super().__init__(message)