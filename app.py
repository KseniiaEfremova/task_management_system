from flask import Flask, render_template, jsonify
from flask_cors import CORS
from db_utils import get_all_projects, DB_NAME


app = Flask(__name__)
CORS(app)


# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route("/projects")
def get_projects():
    project_table = "projects"
    res = dict(get_all_projects(DB_NAME, project_table))
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
