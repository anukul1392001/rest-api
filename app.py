from flask import Flask , request
from flask.json import jsonify

app = Flask(__name__)
@app.route('/<string:name>', methods=['POST'])
def get(name):
    get_val(name)
    return {'data' : 'ANSHU' }



def  get_val(name):
    val =name
    print(val)
    return None 
    




    

if __name__ == '__main__':
   app.run(debug=True)

