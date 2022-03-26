import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello():
    if( request.method == 'GET'):
        data = {
            "status" : "ok",
            "message" : "Hello World !"
        }
        return jsonify(data)
    else : 
        return jsonify({})


if __name__ == "__main__":
    app.run()
