from flask import Flask, render_template , request
from flask import url_for ,jsonify


app = Flask(__name__, template_folder='templates')
@app.route('/veg', methods=['GET'])
def get():
    arg = request.args
    data = arg.get('name')
    return render_template('index.html',name = data)


@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    return jsonify(name)

response = {
    'Success' : 'True'
}


if __name__ == '__main__':
   app.run(debug=True)

