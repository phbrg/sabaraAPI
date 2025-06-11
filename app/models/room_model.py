from sqlalchemy import Column, Integer, Float, DateTime
from app.db.connection import Base
from datetime import datetime

class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    luminosity = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)