# crud.py
from sqlalchemy.orm import Session
from . import models
from typing import List

def create_prediction(
    db: Session, 
    features: List,  # This will be your input list
    prediction: float,
    probability: float,
) -> models.Prediction:
    # Create dictionary mapping features to model columns
    prediction_data = {
        'seniority': int(features[0]),
        'home': features[1],
        'time': int(features[2]),
        'age': int(features[3]),
        'marital': features[4],
        'records': features[5],
        'job': features[6],
        'expenses': float(features[7]),
        'income': float(features[8]),
        'assets': float(features[9]),
        'debt': float(features[10]),
        'amount': float(features[11]),
        'price': float(features[12]),
        'prediction': prediction,
        'probability': probability
    }
    
    # Create new prediction record
    db_prediction = models.Prediction(**prediction_data)
    
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def get_prediction(db: Session, prediction_id: int):
    return db.query(models.Prediction).filter(models.Prediction.id == prediction_id).first()

def get_all_predictions(db: Session):
    return db.query(models.Prediction).all()