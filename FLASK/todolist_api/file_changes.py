import json


def read_tasks_from_file(file_path='tasks.json'):
    try:
        with open(file_path, 'r') as f:
            tasks = json.load(f)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error reading tasks from file: {error}")
        return {}


def write_changes_to_file(tasks, file_path='tasks.json'):
    try:

        # This sorts the tasks after a criteria, in this care being the value of the dictionary, 'name'
        # To redo with importance as a criteria
        sorted_tasks = {k: v for k, v in sorted(tasks.items(), key=lambda task: task[1]['name'])}

        with open(file_path, 'w') as f:
            json.dump(sorted_tasks, f, indent=2)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error writing tasks to file: {e}")

