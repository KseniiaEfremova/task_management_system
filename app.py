from flask import Flask, render_template, jsonify, request
from db_utils import get_all_projects, add_new_task, DB_NAME, delete_task_fromDB

app = Flask(__name__)
app.secret_key = 'paskudzio'


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/projects")
def get_projects():
    project_table = "projects"
    res = dict(get_all_projects(DB_NAME, project_table))
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


@app.route("/delete_task/<int:task_id>", methods=['DELETE'])
def delete_task_route(task_id):
    delete_task_fromDB(task_id)
    return f"Task with ID: {task_id} successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)


