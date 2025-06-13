from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.connection import getDb
from app.schemas.room_schema import RoomCreate, RoomOut
from app.utils.guards import getCurrentUser
from app.controllers.room_controller import createRoom, getRoom

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

@router.post('/create', response_model=RoomOut)
def createRoomRoute(roomData: RoomCreate, db: Session = Depends(getDb)):
    return createRoom(roomData, db)

@router.get('/', response_model=List[RoomOut])
def getRoomRoute(id: Optional[int] = Query(default=None), temperature: Optional[float] = Query(default=None), humidity: Optional[float] = Query(default=None), light: Optional[float] = Query(default=None), db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return getRoom(id, temperature, humidity, light, db)