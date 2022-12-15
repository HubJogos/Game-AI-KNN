from hashlib import new
from typing import List
from flask import Flask, jsonify, request
from joblib import load
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route("/kneighbors", methods=['GET', 'POST'])
def knn():
    if request.method == 'POST':

        key = request.form['key']
        key = key.split(",")

        new_key = np.array(key)
        y = new_key.astype(np.float)
    
        model = load("knnmodelTESTE.joblib")
        #print(model)
        predict = model.kneighbors([y])
        print([y])
        print(predict)
        return jsonify({"Mapas": np.array(predict).tolist()})
    else:
        return 'working'

if __name__ == '__main__':
    app.run(debug=True)