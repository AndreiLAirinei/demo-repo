from flask import Flask, request, make_response
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
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    data = controller_instance.get(task_id)
    response = make_response(data)
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


@app.route('/tasks/<task_id>', methods=['PUT'])
def put_task(task_id):
    data = controller_instance.put(task_id)
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks/<task_id>/<updated_field>', methods=['PATCH'])
def patch_task(task_id, updated_field):
    updated_field = request.json.get(updated_field)

    if updated_field is None:

        data = {'error': 'Invalid field'}
    else:
        data = controller_instance.patch(task_id, updated_field)

    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/tasks/<task_id>/status', methods=['PATCH'])
def status_update(task_id):
    status_data = request.json.get('status')

    if status_data == 'Done':
        data = controller_instance.update_status_to_done(task_id)
    else:
        data = {'error': 'Invalid status update'}

    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':

    type_of_repository = 1  # =json / 2 = csv
    app.run(debug=True)
