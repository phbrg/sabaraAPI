from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.db.connection import Base
import enum

class AppointmentType(enum.Enum):
    PARTICULAR = 'particular'
    SUS = 'SUS'
    CONVENIO = 'convenio'

class Appointment(Base):
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    medic_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime)
    appointmentType = Column(Enum(AppointmentType))

    patient = relationship('Patiente')
    medic = relationship('User')