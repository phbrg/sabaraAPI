from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.connection import Base
import enum

class StatusEnum(enum.Enum):
    PENDENTE = 'pendente'
    RESOLVIDO = 'resolvido'
    INTERNACAO = 'internacao'
    MEDICACAO = 'medicacao'

class Prontuario(Base):
    __tablename__ = 'prontuario'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    medic_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String)
    status = Column(Enum(StatusEnum))

    patient = relationship('Patient')
    medic = relationship('User')