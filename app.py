from flask import Flask, render_template, jsonify
from db_utils import get_all_projects, DB_NAME


app = Flask(__name__)
app.secret_key = 'paskudzio'


# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route("/projects")
def get_projects():
    project_table = "projects"
    res = dict(get_all_projects(DB_NAME, project_table))
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
