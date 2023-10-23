import requests
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'paskudzio'

@app.route('/')
def home():
    return render_template('index.html')

def delete_project(project_name):
    response = requests.delete(f"http://127.0.0.1:5001/delete_project/<int:project_name>")
    if response.status_code == 200:
        print(f"Project: {project_name} has successfully been deleted")
    else:
        print(f"Failed to delete project.")

if __name__ == '__main__':
    app.run(debug=True)

