from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from app.models.appointment_model import AppointmentType

class AppointmentCreate(BaseModel):
    patient_id: int
    medic_id: int
    date: str
    appointmentType: AppointmentType

class AppointmentOut(BaseModel):
    patient_id: int
    medic_id: int
    date: datetime
    appointmentType: AppointmentType

    class Config:
        orm_mode = True

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int] = None
    medic_id: Optional[int] = None
    date: Optional[str] = None
    appointmentType: Optional[AppointmentType] = None