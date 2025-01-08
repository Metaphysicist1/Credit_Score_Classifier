import joblib
import numpy as np
from typing import Tuple
import logging
from core.config import settings
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

            dv = DictVectorizer(sparse=False)

            # train_dicts = data.fillna(0).to_dict(orient='records')
            processed_data = dv.fit_transform([input_data])
            features = xgb.DMatrix(processed_data)

            prediction = self.model.predict(features)
            probability = self.model.predict_proba(features).max()
            
            return float(prediction), float(probability)
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise RuntimeError("Prediction failed")

    def get_model_version(self) -> str:
        return self.model_version 