import json
from flask import Flask, request ,url_for
from flask.json import jsonify

app = Flask(__name__)
@app.route('/veg', methods=['GET'])
def get():
    return "PointBlank<.>"


@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    print(url_for('query_records'))

    return jsonify(name)

response = {
    'Success' : 'True'
}

@app.route('/post', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    return jsonify(record)


if __name__ == '__main__':
   app.run(debug=True)

