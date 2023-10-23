from flask import Flask, render_template, jsonify
from db_utils import delete_project


app = Flask(__name__)
app.secret_key = 'paskudzio'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/delete_project/<int:project_id>', methods=['DELETE'])
def delete_project_route(project_id):
    result = delete_project(project_id)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
