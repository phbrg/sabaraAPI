from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from app.db.connection import Base

class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    allergies = Column(ARRAY(String), nullable=True)
    notes = Column(ARRAY(String), nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow)