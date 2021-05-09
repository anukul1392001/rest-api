# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/helloesp', method = ['GET'])
def helloHandler():
    return 'Hello ESP8266, from Flask'
 
app.run(host='0.0.0.0', port= 8090)
