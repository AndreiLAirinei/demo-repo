import json
from exceptions import FileError, FileNotFoundError, JSONDecodeError


def read_tasks_from_file(file_path='tasks.json'):
    default_value = {}

    try:
        with open(file_path, "r") as file:
            tasks_data = json.load(file)
        return tasks_data

    except FileNotFoundError as file_error:
        print(f"Error writing tasks to file: {file_error}")
    except JSONDecodeError as json_error:
        print(f"Error writing tasks to file: {json_error}")
    except FileError as file_error:
        print(f"Error reading tasks from file: {file_error}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return default_value


def write_changes_to_file(new_task, file_path='tasks.json'):
    try:
        existing_tasks = read_tasks_from_file()
        existing_tasks.update(new_task)

        with open(file_path, "w") as file:
            json.dump(existing_tasks, file, indent=2, separators=(',', ': '), default=str)

    except FileNotFoundError as file_error:
        print(f"Error writing tasks to file: {file_error}")
    except JSONDecodeError as json_error:
        print(f"Error writing tasks to file: {json_error}")
    except FileError as file_error:
        print(f"Error writing tasks to file: {file_error}")

        # # Sort tasks by 'priority'
        # sorted_tasks = sorted(existing_tasks.items(), key=lambda x: x[1].get('priority'), reverse=True)
        # # Convert the sorted tasks to a dictionary
        # sorted_tasks_dict = {k: v for k, v in sorted_tasks}
