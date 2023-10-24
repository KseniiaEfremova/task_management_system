from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from db_utils import get_all_projects, add_new_task, DB_NAME, insert_new_project, get_tasks_by_status, get_task_by_id
tasks_table = 'tasks'
projects_table = 'projects'


app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def handle_404(error):
    response = make_response(jsonify({'error': 'page not found'}), 404)
    return response


@app.errorhandler(500)
def handle_500(error):
    response = make_response(jsonify({'error': 'server is down, contact one of Coding Stars United Developer'}), 500)
    return response


@app.route("/projects")
def get_projects():
    projects = get_all_projects(DB_NAME, projects_table)
    res = []
    for project in projects:
        id_and_name_project = dict()
        id_and_name_project["project_id"] = project[0]
        id_and_name_project["project_name"] = project[1]
        res.append(id_and_name_project)
    return jsonify(res)


@app.route('/projects/<project_id>id/<task_id>', endpoint='get_taksks_per_project_by_id')
def get_task_per_project_by_id(project_id, todo_id):
    response = get_task_by_id(DB_NAME, tasks_table, project_id, todo_id)
    return jsonify(response)


@app.route("/projects/<project_id>/<status>", endpoint='get_tasks_per_project_by_status')
def get_tasks_per_project_by_status(project_id, status):
    res = get_tasks_by_status(DB_NAME, tasks_table, project_id, status)
    return jsonify(res)


@app.route("/newproject", methods=['POST'])
def add_project():
    """
    Add a new project to the database. This endpoint allows clients to add a new project to the database.
    Parameters:
    None (uses JSON data from the request body)
    Returns:
    JSON: If the project is successfully added, returns the new project data with a 201 status code.
          If the request data is invalid, returns an error message with a 400 status code.
          If an error occurs during processing, returns an error message with a 500 status code.
    """
    try:
        new_project = request.get_json()

        if new_project:
            table_name = new_project['table_name']
            project_name = new_project['project_name']

            insert_new_project(DB_NAME, table_name, project_name)
            return jsonify(new_project), 201
        else:
            return jsonify({'message': 'Invalid data'}), 400

    except Exception as exc:
        print(f"An error occurred: {str(exc)}")
        return jsonify({'message': 'An error occurred'}), 500


@app.route("/newtask", methods=['POST'])
def adding_task():
    """ adding_task() function handles POST requests made to /newtask,
    try the new_task variable receives JSON data, parses it into a Python dict 
    if data for new_task has been recieved - this is extracted into variables
    these are passed as params into the add_new_task() function, which is called
    new task data is and a status code of 201, indicating success.
    else if received JSON data is invalid or missing, and error message and status code of 400 is returned
    except used to catch exceptions, which will print the exception and return an error
    """
    try:
        new_task = request.get_json()

        if new_task:
            table_name = tasks_table
            project_id = new_task['project_id']
            description = new_task['description']
            deadline = new_task['deadline']
            status = new_task['status']

            add_new_task(DB_NAME, table_name, project_id, description, deadline, status)

            return jsonify(new_task), 201
        else:
            return jsonify({'message': 'Invalid data'}), 400
    except Exception as exc:
        print(f"An error occurred: {str(exc)}")
        return jsonify({'message': 'An error occurred'}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)
