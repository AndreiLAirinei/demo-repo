
class FileNotFoundError(Exception):
    def __init__(self, message="File not found"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


class JSONDecodeError(Exception):
    def __init__(self, message="Error decoding JSON"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


class TaskNotFoundError(Exception):
    def __init__(self, task_id, status_code=404, message="Task does not exist"):
        super().__init__(message)
        self.task_id = task_id
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code}: {self.message} (Task ID: {self.task_id})"


class InvalidTaskIdError(Exception):
    def __init__(self, task_id, status_code=400, message="Invalid task ID"):
        super().__init__(message)
        self.task_id = task_id
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code}: {self.message} (Task ID: {self.task_id})"


class ParsingError(Exception):
    def __init__(self, status_code=400, message="Required fields are missing (*args)"):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code}: {self.message}"


class RepositoryError(Exception):
    def __init__(self, status_code=500, message="Repository error occurred."):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code}: {self.message}"


class FieldNotFoundError(Exception):
    def __init__(self, field_name, task_id, status_code=404, message="Field not found"):
        super().__init__(message)
        self.message = message
        self.field_name = field_name
        self.task_id = task_id
        self.status_code = status_code

    def __str__(self):
        return f"{self.status_code}: {self.message} - {self.field_name} (Task ID: {self.task_id})"
