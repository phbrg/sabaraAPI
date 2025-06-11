from pydantic import BaseModel
from datetime import datetime

class RoomCreate(BaseModel):
    temperature: float
    humidity: float
    luminosity: float
    date: datetime