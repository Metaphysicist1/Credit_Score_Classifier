import logging
import sys
from logging.handlers import RotatingFileHandler
from .config import settings
import os

def setup_logging():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("app")
    logger.setLevel(settings.LOG_LEVEL)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s: %(message)s')
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger 