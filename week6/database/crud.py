# crud.py
from sqlalchemy.orm import Session
from . import models
from app.models.domain import schemas
from datetime import datetime

def create_prediction(
    db: Session, 
    prediction: float, 
    probability: float, 
    model_version: str
):
    db_prediction = models.Prediction(
        prediction=prediction,
        probability=probability,
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def get_prediction(db: Session, prediction_id: int):
    return db.query(models.Prediction).filter(models.Prediction.id == prediction_id).first()

def get_all_predictions(db: Session):
    return db.query(models.Prediction).all()