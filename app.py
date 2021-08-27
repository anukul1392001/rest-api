from flask import Flask , request
from flask.json import jsonify

app = Flask(__name__)
@app.route('/veg', methods=['GET'])
def get():
    return "Sreeniketh Jod"


if __name__ == '__main__':
   app.run(debug=True)

