from flask import Flask , request
from flask.json import jsonify

app = Flask(__name__)
@app.route('/<string:name>', methods=['GET'])
def get(name):
    get_val(name)
    return {'data' : name }



def  get_val(name):
    val =name
    print(val)
    return None 
    




    

if __name__ == '__main__':
   app.run(debug=True)

