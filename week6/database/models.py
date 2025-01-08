from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Prediction(Base):
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