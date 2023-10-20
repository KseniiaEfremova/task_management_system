from flask import Flask, render_template, jsonify
from db_utils import get_all_projects, DB_NAME


app = Flask(__name__)
app.secret_key = 'paskudzio'


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/projects", methods=["GET"])
def get_projects():
    res = get_all_projects(DB_NAME)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
