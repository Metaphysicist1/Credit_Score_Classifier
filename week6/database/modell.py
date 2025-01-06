from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PredictionResult(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True,index=True)
    seniority =Column(Integer)
    home = Column(String)
    time = Column(Integer)
    age = Column(Integer)
    marital = Column(String)
    records = Column(String)
    job = Column(String)
    expenses = Column(Float)
    income = Column(Float)
    assets = Column(Float)
    debt = Column(Float)
    amount = Column(Float)
    price = Column(Float)
    prediction = Column(Float)