from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb 
from pydantic import BaseModel
import joblib
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained Decision Tree model
try:
    model = joblib.load("models/xgboost_classifier.pkl")
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    features: list

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>FastAPI Prediction Service</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #333; }
                label { display: block; margin: 10px 0 5px; }
                input, select { width: 100%; padding: 8px; margin-bottom: 10px; }
                button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
                button:hover { background-color: #45a049; }
                .result { margin-top: 20px; }
            </style>
        </head>
        <body>
            <h1>FastAPI Prediction Service</h1>
            <form id="prediction-form">
                <label for="seniority">Seniority:</label>
                <input type="number" id="seniority" name="seniority" required>

                <label for="home">Home:</label>
                <select id="home" name="home" required>
                    <option value="rent">Rent</option>
                    <option value="own">Own</option>
                </select>

                <label for="time">Time:</label>
                <input type="number" id="time" name="time" required>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required>

                <label for="marital">Marital Status:</label>
                <select id="marital" name="marital" required>
                    <option value="single">Single</option>
                    <option value="married">Married</option>
                    <option value="separated">Separated</option>
                    <option value="divorced">Divorced</option>
                </select>

                <label for="records">Records:</label>
                <select id="records" name="records" required>
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                </select>

                <label for="job">Job Type:</label>
                <select id="job" name="job" required>
                    <option value="fixed">Fixed</option>
                    <option value="variable">Variable</option>
                </select>

                <label for="expenses">Expenses:</label>
                <input type="number" id="expenses" name="expenses" required>

                <label for="income">Income:</label>
                <input type="number" id="income" name="income" required>

                <label for="assets">Assets:</label>
                <input type="number" id="assets" name="assets" required>

                <label for="debt">Debt:</label>
                <input type="number" id="debt" name="debt" required>

                <label for="amount">Amount:</label>
                <input type="number" id="amount" name="amount" required>

                <label for="price">Price:</label>
                <input type="number" id="price" name="price" required>

                <button type="submit">Predict</button>
            </form>

            <div class="result" id="result"></div>

            <script>
                document.getElementById('prediction-form').onsubmit = async function(event) {
                    event.preventDefault();
                    const formData = new FormData(this);
                    const data = {};
                    formData.forEach((value, key) => {
                        data[key] = value;
                    });

                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ features: Object.values(data) }),
                    });

                    const result = await response.json();
                    document.getElementById('result').innerText = 'Based on the prediction model, the probability of being classified as high risk: ' + result.prediction;
                };
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/predict")
def predict(data: InputData):
    try:
        logger.info("Start number dict")
        input_data = {
            'seniority': int(data.features[0]),  # Convert to int
            'home': data.features[1],              # Categorical
            'time': int(data.features[2]),        # Convert to int
            'age': int(data.features[3]),         # Convert to int
            'marital': data.features[4],           # Categorical
            'records': data.features[5],           # Categorical
            'job': data.features[6],               # Categorical
            'expenses': float(data.features[7]),   # Convert to float
            'income': float(data.features[8]),      # Convert to float
            'assets': float(data.features[9]),      # Convert to float
            'debt': float(data.features[10]),       # Convert to float
            'amount': float(data.features[11]),     # Convert to float
            'price': float(data.features[12]),      # Convert to float
        }

        logger.info("Start dict vect")
        dv = DictVectorizer(sparse=False)

        # train_dicts = data.fillna(0).to_dict(orient='records')
        processed_data = dv.fit_transform([input_data])
        features = xgb.DMatrix(processed_data)
        # Make prediction
        prediction = model.predict(features)
        logger.info(f"Prediction made successfully: {float(prediction[0])}")
        return {"prediction": float(prediction[0])}

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=400, detail="Error during prediction")

