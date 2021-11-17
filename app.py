import json
from flask import Flask, request ,url_for
from flask.json import jsonify

app = Flask(__name__)
@app.route('/veg', methods=['GET'])
def get():
    return render_template


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
    record = request.form
    print(record)
    print(record['Id'])
    print(record['Name'])
    print(record['Value'])
    print(url_for('update_record'))

    return  record#jsonify(record)


if __name__ == '__main__':
   app.run(debug=True)

