# XGBoost Prediction API

## Description
This project is a Flask-based web application that predicts diamond prices based on various input features using an XGBoost model.

## Folder Structure

├── data
│   └── diamonds.csv
├── Dockerfile
├── models
│   ├── model.joblib
│   └── scaler.joblib
├── Pipfile
├── Pipfile.lock
├── predict.py
├── README.md
├── requirements.txt
├── scripts
│   ├── 01_explore.ipynb
│   └── exp.ipynb
└── server.py


## Installation

Clone this repo:
```
https://github.com/Metaphysicist1/ml-zoomcamp.git
```

Or pull docker Image
```
docker pull metaphysicist/diamond-price-predictor:latest
```


To set up the project, ensure you have Docker installed. Then, build and run the Docker container:
```
docker build -t xgboost-predictor .
```
```
docker run -p 9612:9612 xgboost-predictor
```

## Usage
To make predictions, send a POST request to the `/predict` endpoint with the diamond data in JSON format. Here’s an example using `curl`:
```
curl -X POST http://localhost:9612/predict -H "Content-Type: application/json" -d '{
    "carat": {"53556": 0.5},
    "depth": {"53556": 60},
    "table": {"53556": 55},
    "x": {"53556": 5.0},
    "y": {"53556": 5.0},
    "z": {"53556": 3.0},
    "clarity_encoded": {"53556": 0},
    "cut_encoded": {"53556": 1},
    "color_encoded": {"53556": 2}
}'
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
