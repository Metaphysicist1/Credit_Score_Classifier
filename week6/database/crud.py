# crud.py
from sqlalchemy.orm import Session
from database.modell import PredictionResult

def create_prediction(db: Session, prediction_data: dict):
    prediction = PredictionResult(**prediction_data)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

def get_prediction(db: Session, prediction_id: int):
    return db.query(PredictionResult).filter(PredictionResult.id == prediction_id).first()

def get_all_predictions(db: Session):
    return db.query(PredictionResult).all()