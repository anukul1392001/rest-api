# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/helloesp', methods = ['GET'])
def helloHandler():
    return 'Hello ESP8266, from Flask'


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

 
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
