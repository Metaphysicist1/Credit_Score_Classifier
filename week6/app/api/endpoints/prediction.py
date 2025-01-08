import sys
import os

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse


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




@router.get("/", response_class=HTMLResponse)
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


@router.post("/predict", response_model=schemas.PredictionOutput)
def create_prediction(data: schemas.PredictionInput, db: Session = Depends(get_db)):
    try:
    
        # print(data,'\n\n\n\n',type(data))

        # print(data.features)



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