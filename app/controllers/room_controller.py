from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status, Query
from typing import Optional
from datetime import datetime
from app.models.room_model import Room
from app.schemas.room_schema import RoomCreate

def createRoom(roomData: RoomCreate, db: Session):
    newRoom = Room(
        temperature=roomData.temperature,
        humidity=roomData.humidity,
        light=roomData.light,
    )
    db.add(newRoom)
    db.commit()
    db.refresh(newRoom)

    return newRoom

def getRoom(id: Optional[int], temperature: Optional[float], humidity: Optional[float], light: Optional[float], db: Session):
    query = db.query(Room)
    
    if id is not None:
      query = query.filter(Room.id == id)
    if temperature is not None:
      query = query.filter(Room.temperature == temperature)
    if humidity is not None:
      query = query.filter(Room.humidity == humidity)
    if light is not None:
      query = query.filter(Room.light == light)
    
    return query.all()