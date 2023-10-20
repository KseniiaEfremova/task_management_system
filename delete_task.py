from flask import Flask, jsonify
from db_utils import delete_task

app = Flask(__name__)

@app.route('/delete_task', methods=['DELETE'])
def delete_task_route():
    result = delete_task()
    return jsonify(result)

