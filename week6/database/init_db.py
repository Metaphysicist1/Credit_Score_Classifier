from sqlalchemy import create_engine
from modell import Base
from db import DATABASE_URL

engine = create_engine(DATABASE_URL)

# Create the database tables
Base.metadata.create_all(bind=engine)