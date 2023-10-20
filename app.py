from flask import Flask, render_template, jsonify
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


@app.route("/newtask", methods=['PUT'])
def adding_task():
    new_task = request.get_json()
    {
        "project_id": input_project_id,
        "description": input_description,
        "deadline": formatted_deadline_date,
        "status": input_status,
    }



if __name__ == '__main__':
    app.run(debug=True)
