from flask import Flask, render_template, jsonify, make_response
from db_utils import get_all_projects, DB_NAME


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


if __name__ == '__main__':
    app.run(debug=True)
