from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class PatientCreate(BaseModel):
    full_name: str
    birth_date: date
    cpf: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    allergies: Optional[str] = None
    notes: Optional[str] = None

class PatientOut(BaseModel):
    id: int
    full_name: str
    birth_date: date
    cpf: str
    phone: Optional[str]
    email: Optional[EmailStr]
    allergies: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True