import json

with open('tasks.json', 'r') as f:
    tasks = json.load(f)


def write_changes_to_file():
    global tasks
    # This sorts the tasks after a criteria, in this care being the value of the dictionary, 'name'
    tasks = {k: v for k, v in sorted(tasks.items(), key=lambda task: task[1]['name'])}
    # Creates a file 'tasks' if one is not found in the folder
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
