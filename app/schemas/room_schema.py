from pydantic import BaseModel
from datetime import datetime
from app.models.user_model import RoleEnum

class RoomCreate(BaseModel):
    temperature: float
    humidity: float
    light: float

class RoomOut(BaseModel):
    id: int
    temperature: float
    humidity: float
    light: float
    createdAt: datetime

    class Config:
        orm_mode = True