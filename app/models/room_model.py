from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.connection import Base

class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    light = Column(Float, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)