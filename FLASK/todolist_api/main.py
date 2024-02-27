from flask import Flask, jsonify, make_response
from TaskController import Controller
from Repository import JSONRepository

app = Flask(__name__)

repository = JSONRepository()
controller_instance = Controller(repository=repository)

# def type_of_repository(var):
#     if var == 1:
#         repository = JSONRepository()
#      elif var == 2:
#          repository = CSVRepository()


# Functions from controller for each url
# @app for PUT/PATCH/DELETE


@app.route('/tasks', methods=['GET'])
@app.route('/tasks/all', methods=['GET'])
def get_all_tasks():
    data = controller_instance.get(task_id="all")
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    data = controller_instance.get(task_id)
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks', methods=['POST'])
def post_task():
    data = controller_instance.post()
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = controller_instance.delete(task_id)
    return result


if __name__ == '__main__':

    type_of_repository = 1  # =json / 2 = csv
    app.run(debug=True)
