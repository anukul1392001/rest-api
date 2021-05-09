# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/helloesp', methods = ['GET'])
def helloHandler():
    return 'Hello ESP8266, from Flask'
 
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
