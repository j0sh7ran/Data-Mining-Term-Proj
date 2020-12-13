# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request
from flask_cors import CORS
import pickle

## for unzipping the finalized_model.zip ##
'''
import zipfile
with zipfile.ZipFile('finalized_model.zip', 'r') as zip_ref:
    zip_ref.extractall()
'''


app = Flask(__name__)
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Result: Please give a value'

@app.route('/review', methods=['GET', 'POST'])
def generate_prediction():
    if(request.method == 'POST'):
        text = request.form.get('review')
        item = [text]
        prediction = loaded_model.predict(item)
        result = str(prediction[0]) + " out of 10.0"
    else:
        result="ERROR IN PROCESSING"
    return result
