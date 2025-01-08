from fastapi import FastAPI
from api.endpoints import prediction
from core.config import settings
from core.logging import setup_logging
from database.models import Base
from database.session import engine

# Setup logging
logger = setup_logging()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers
app.include_router(
    prediction.router,
    prefix=f"{settings.API_V1_STR}/predictions",
    tags=["predictions"]
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}