from flask import Flask , request
from flask.json import jsonify

app = Flask(__name__)
@app.route('/<string:name>')
def get(name):
    get_val(name)
    return 'name'



def  get_val(name):
    val =name
    print(val)
    return None 
    




    

if __name__ == '__main__':
   app.run(host='192.168.43.112',port='5000',debug=True)

