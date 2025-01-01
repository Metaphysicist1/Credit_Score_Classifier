import requests


url = "http://localhost:9612/predict"

data = {"carat":{"53556":-0.0807739524},"depth":{"53556":-0.1701729396},"table":{"53556":-1.1032829874},"x":{"53556":0.1226521897},"y":{"53556":0.1425428612},"z":{"53556":0.1140366698},"clarity_encoded":{"53556":-0.4835043278},"cut_encoded":{"53556":-0.5407619745},"color_encoded":{"53556":-0.3479486993}}

response = requests.post(url,json=data).json()

print(response)
