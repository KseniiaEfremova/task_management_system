from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/delete_task')
def delete_task():
    return 'deleted'

if __name__ == '__main__':
    app.run(debug=True)