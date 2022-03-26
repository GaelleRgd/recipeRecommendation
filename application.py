import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200


if __name__ == "__main__":
    app.run()