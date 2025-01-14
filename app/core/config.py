from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API configs
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ML Prediction Service"
    
    # Database configs
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str 
    POSTGRES_PORT: int 

    # ML Model configs
    MODEL_PATH: str = "app/models/ml/xgboost_classifier.pkl"
    
    # Logging configs
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"
    
    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields

settings = Settings() 

print(settings.dict()) 