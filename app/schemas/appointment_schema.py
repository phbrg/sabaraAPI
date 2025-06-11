from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.models.appointment_model import AppointmentType

class AppointmentCreate(BaseModel):
    patient_id: int
    medic_id: int
    date: datetime
    tipo: AppointmentType