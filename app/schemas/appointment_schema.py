from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from app.models.appointment_model import AppointmentType

class AppointmentCreate(BaseModel):
    patient_id: int
    patient_name: str
    medic_id: int
    medic_name: str
    date: str
    appointmentType: AppointmentType

class AppointmentOut(BaseModel):
    patient_id: int
    patient_name: str
    medic_id: int
    medic_name: str
    date: datetime
    appointmentType: AppointmentType

    class Config:
        orm_mode = True

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int] = None
    patient_name: Optional[str] = None
    medic_id: Optional[int] = None
    medic_name: Optional[str] = None
    date: Optional[str] = None
    appointmentType: Optional[AppointmentType] = None