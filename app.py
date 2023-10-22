from flask import Flask, jsonify
from db_utils import delete_task

app = Flask(__name__)


@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    delete_task(task_id)
    return f"Task with ID: {task_id} successfully deleted"
