from flask import Flask, render_template, jsonify
from db_utils import get_all_projects, get_tasks_by_status, DB_NAME

tasks_table = 'tasks'


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


@app.route("/projects/<project_id>/<status>")
def get_tasks_per_project_by_status(project_id, status):
    res = get_tasks_by_status(DB_NAME, tasks_table, project_id, status)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
