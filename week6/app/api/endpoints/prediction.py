import sys
import os

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.append(app_dir)

from app.models.domain import schemas
from app.services.ml_service import MLService





from database.session import get_db
from database import crud
import logging

router = APIRouter()
ml_service = MLService()
logger = logging.getLogger("app")







@router.post("/predict", response_model=schemas.PredictionOutput)
def create_prediction(
    data: schemas.PredictionInput,
    db: Session = Depends(get_db)
):
    try:
        # Make prediction
        prediction, probability = ml_service.predict(data.features)
        
        # Save to database
        db_prediction = crud.create_prediction(
            db=db,
            prediction=prediction,
            probability=probability,
            model_version=ml_service.get_model_version()
        )
        
        logger.info(f"Successful prediction created with id: {db_prediction.id}")
        return db_prediction
        
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/prediction/{prediction_id}", response_model=schemas.PredictionOutput)
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = crud.get_prediction(db, prediction_id)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction 