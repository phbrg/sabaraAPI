from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.connection import getDb
from app.schemas.user_schema import UserCreate, UserOut, UserLogin, UserUpdate
from app.utils.guards import getCurrentUser, isAdmin
from app.controllers.user_controller import createUser, loginUser, meUser, updateUser, deleteUser, getUser

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

@router.post('/create', response_model=UserOut)
def createUserRoute(userData: UserCreate, db: Session = Depends(getDb)):
    return createUser(userData, db)

@router.post('/login')
def login(user: UserLogin, db: Session = Depends(getDb)):
    return loginUser(user, db)

@router.get('/me')
def getMeRoute(db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return meUser(user, db)

@router.put('/update/{userId}', response_model=UserOut)
def updateUserRoute(userId: int, userData: UserUpdate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return updateUser(userId, userData, db)

@router.delete('/delete/{userId}')
def deleteUserRoute(userId: int, db: Session = Depends(getDb), user: dict = Depends(isAdmin)):
    return deleteUser(userId, db)

@router.get('/', response_model=List[UserOut])
def getUserRoute(id: Optional[int] = Query(default=None), name: Optional[str] = Query(default=None), email: Optional[str] = Query(default=None), db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return getUser(id, name, email, db)