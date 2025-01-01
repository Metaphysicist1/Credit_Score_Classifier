import json
from flask import Flask, request, jsonify
from matplotlib import dviread
import joblib
import pandas as pd
import requests


app = Flask('xgboost')



# data = {"carat":{"53556":-0.0807739524},"depth":{"53556":-0.1701729396},"table":{"53556":-1.1032829874},"x":{"53556":0.1226521897},"y":{"53556":0.1425428612},"z":{"53556":0.1140366698},"clarity_encoded":{"53556":-0.4835043278},"cut_encoded":{"53556":-0.5407619745},"color_encoded":{"53556":-0.3479486993}}



@app.route('/predict',methods=['POST'])
def predict():
    data = request.json

    data = pd.DataFrame(data)
    model = joblib.load('models/model.joblib')
    price = model.predict(data)
    result = {"Based on providen diamond data it costs:":float(price)}
    return jsonify({"message": f"{result}"}), 200


if __name__=="__main__":
    app.run(debug=True, host='localhost', port='9612')

    