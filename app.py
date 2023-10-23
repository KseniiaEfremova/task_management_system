from flask import Flask, render_template, jsonify, request
from db_utils import get_all_projects, add_new_task, DB_NAME


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
    new_task variable receives JSON data, parses it into a Python dict 
    if data for new_task has been recieved - this is extracted into variables
    these are passed as params into the add_new_task() function, which is called
    new task data is and a status code of 201, indicating success.
    else if received JSON data is invalid or missing, and error message and status code of 400 is returned
    """
    new_task = request.get_json()

    if new_task:
        project_id = new_task['project_id']
        description = new_task['description']
        deadline = new_task['deadline']
        status = new_task['status']

        add_new_task(project_id, description, deadline, status)

        return jsonify(new_task), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)
