from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class PatientCreate(BaseModel):
    full_name: str
    birth_date: str
    cpf: str
    phone: str
    email: EmailStr
    allergies: Optional[List[str]] = None
    notes: Optional[List[str]] = None

class PatientOut(BaseModel):
    id: int
    full_name: str
    birth_date: datetime
    cpf: str
    phone: str
    email: EmailStr
    allergies: Optional[List[str]]
    notes: Optional[List[str]]
    createdAt: datetime

    class Config:
        orm_mode = True

class PatientUpdate(BaseModel):
    full_name: Optional[str] = None
    birth_date: Optional[str] = None
    cpf: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    allergies: Optional[List[str]] = None
    notes: Optional[List[str]] = None