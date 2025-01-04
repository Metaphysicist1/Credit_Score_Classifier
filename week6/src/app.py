from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained Decision Tree model
# try:
#     model = joblib.load("decision_tree_model.pkl")
#     logger.info("Model loaded successfully.")
# except Exception as e:
#     logger.error(f"Error loading model: {e}")
#     raise

app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input features to numpy array
        features = np.array(data.features).reshape(1, -1)
        # Make prediction
        # prediction = model.predict(features)
        # logger.info(f"Prediction made successfully: {prediction[0]}")
        # return {"prediction": prediction[0]}
        
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=400, detail="Error during prediction")
