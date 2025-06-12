from sqlalchemy import Column, Integer, String, Date
from app.db.connection import Base

class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    allergies = Column(String, nullable=True)
    notes = Column(String, nullable=True)