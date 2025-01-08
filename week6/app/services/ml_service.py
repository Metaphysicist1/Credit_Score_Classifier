import joblib
import numpy as np
from typing import Tuple
import logging
from app.core.config import settings
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb 
from pydantic import BaseModel

logger = logging.getLogger("app")

class InputData(BaseModel):
    features: list

class MLService:
    def __init__(self):
        self.model = None
        self.model_version = "1.0.0"
        self._load_model()

    def _load_model(self):
        try:
            self.model = joblib.load(settings.MODEL_PATH)
            logger.info(f"Model loaded successfully from {settings.MODEL_PATH}")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise RuntimeError("Failed to load model")

    def predict(self, data: InputData) -> Tuple[float, float]:
        try:
            
            print("\n\n\n",data,"\n\n\n\n")
                  
            input_data = {
                'seniority': int(data[0]),  # Convert to int
                'home': data[1],              # Categorical
                'time': int(data[2]),        # Convert to int
                'age': int(data[3]),         # Convert to int
                'marital': data[4],           # Categorical
                'records': data[5],           # Categorical
                'job': data[6],               # Categorical
                'expenses': float(data[7]),   # Convert to float
                'income': float(data[8]),      # Convert to float
                'assets': float(data[9]),      # Convert to float
                'debt': float(data[10]),       # Convert to float
                'amount': float(data[11]),     # Convert to float
                'price': float(data[12]),      # Convert to float
            }

            dv = DictVectorizer(sparse=False)

            # train_dicts = data.fillna(0).to_dict(orient='records')
            processed_data = dv.fit_transform([input_data])
            features = xgb.DMatrix(processed_data)

            raw_pred = self.model.predict(features)[0]

            probability = 1 / (1 + np.exp(-raw_pred))
            prediction = 1 if probability >= 0.5 else 0
            
            return float(prediction), float(probability)
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise RuntimeError("Prediction failed")

    def get_model_version(self) -> str:
        return self.model_version 