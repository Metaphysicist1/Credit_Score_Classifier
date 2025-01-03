import json
from flask import Flask, request, jsonify, render_template
from matplotlib import dviread
import joblib
import pandas as pd
import requests


app = Flask('xgboost')



# data = {"carat":{"53556":-0.0807739524},"depth":{"53556":-0.1701729396},"table":{"53556":-1.1032829874},"x":{"53556":0.1226521897},"y":{"53556":0.1425428612},"z":{"53556":0.1140366698},"clarity_encoded":{"53556":-0.4835043278},"cut_encoded":{"53556":-0.5407619745},"color_encoded":{"53556":-0.3479486993}}



@app.route('/', methods=['GET'])
def home():
    return '''
        <form action="/predict" method="post">
            Carat: <input type="text" name="carat"><br>
            Depth: <input type="text" name="depth"><br>
            Table: <input type="text" name="table"><br>
            X: <input type="text" name="x"><br>
            Y: <input type="text" name="y"><br>
            Z: <input type="text" name="z"><br>
            Clarity Encoded: <input type="text" name="clarity_encoded"><br>
            Cut Encoded: <input type="text" name="cut_encoded"><br>
            Color Encoded: <input type="text" name="color_encoded"><br>
            <input type="submit" value="Submit">
        </form>
    '''



@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the form
    data = {
        "carat": float(request.form['carat']),
        "depth": float(request.form['depth']),
        "table": float(request.form['table']),
        "x": float(request.form['x']),
        "y": float(request.form['y']),
        "z": float(request.form['z']),
        "clarity_encoded": float(request.form['clarity_encoded']),
        "cut_encoded": float(request.form['cut_encoded']),
        "color_encoded": float(request.form['color_encoded']),
    }

    # Convert to DataFrame for model prediction
    data_df = pd.DataFrame([data])
    model = joblib.load('model.joblib')
    price = model.predict(data_df)

    # Access the first element of the prediction array
    result = {"Based on provided diamond data it costs:": float(price[0])}

    return jsonify({"message": f"{result}"}), 200


if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port='9612')

    