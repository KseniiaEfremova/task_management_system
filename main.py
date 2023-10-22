import requests
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'paskudzio'


@app.route('/')
def home():
    return render_template('index.html')


def delete_task(task_id):
    response = requests.delete(f"http://127.0.0.1:5001/delete_task/<int:task_id>")
    if response.status_code == 204:
        print(f"Task with ID: {task_id} successfully deleted")
    else:
        print(f"Failed to delete task with ID: {task_id}")


if __name__ == '__main__':
    app.run(debug=True)
