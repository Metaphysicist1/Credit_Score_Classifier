from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "postgresql://postgres:edgar2001@localhost:5432/ml"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()