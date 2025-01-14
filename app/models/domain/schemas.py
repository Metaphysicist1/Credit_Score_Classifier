from pydantic import BaseModel
from typing import List, Union

class PredictionInput(BaseModel):
    features: List

class PredictionOutput(BaseModel):
    prediction: float
    probability: float 