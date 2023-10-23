from flask import Flask, render_template, jsonify, make_response, request
from db_utils import get_all_projects, get_tasks_by_status, add_new_task, DB_NAME, delete_project
tasks_table = 'tasks'


app = Flask(__name__)


@app.errorhandler(404)
def handle_404(error):
    response = make_response(jsonify({'error': 'page not found'}), 404)
    return response

@app.errorhandler(500)
def handle_500(error):
    response = make_response(jsonify({'error': 'server is down, contact one of Coding Stars United Developer'}), 500)
    return response

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/projects")
def get_projects():
    project_table = "projects"
    res = dict(get_all_projects(DB_NAME, project_table))
    return jsonify(res)


@app.route("/projects/<project_id>/<status>")
def get_tasks_per_project_by_status(project_id, status):
    res = get_tasks_by_status(DB_NAME, tasks_table, project_id, status)
    return jsonify(res)


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
            table_name = new_task['table_name']
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
