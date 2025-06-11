from pydantic import BaseModel
from enum import Enum
from app.models.prontuario_model import StatusEnum

class ProntuarioCreate(BaseModel):
    patient_id: int
    medic_id: int
    description: str
    status: StatusEnum