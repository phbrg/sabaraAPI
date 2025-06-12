from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime
from app.models.prontuario_model import StatusEnum

class ProntuarioCreate(BaseModel):
    patient_id: int
    patient_name: str
    medic_id: int
    medic_name: str
    description: str

class ProntuarioOut(BaseModel):
    patient_id: int
    patient_name: str
    medic_id: int
    medic_name: str
    description: str
    status: StatusEnum
    createdAt: datetime

    class Config:
        orm_mode = True

class ProntuarioUpdate(BaseModel):
    patient_id: Optional[int] = None
    patient_name: Optional[str] = None
    medic_id: Optional[int] = None
    medic_name: Optional[str] = None
    description: Optional[int] = None
    status: Optional[StatusEnum] = None