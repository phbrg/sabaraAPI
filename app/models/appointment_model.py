from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.connection import Base
from datetime import datetime
import enum

class AppointmentType(enum.Enum):
    PARTICULAR = 'particular'
    SUS = 'SUS'
    CONVENIO = 'convenio'

class Appointment(Base):
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient_name = Column(String)
    medic_id = Column(Integer, ForeignKey('user.id'))
    medic_name = Column(String)
    date = Column(DateTime)
    appointmentType = Column(Enum(AppointmentType))
    createdAt = Column(DateTime, default=datetime.utcnow)

    patient = relationship('Patient')
    medic = relationship('User')