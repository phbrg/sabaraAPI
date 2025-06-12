from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Query
from typing import Optional
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin, UserUpdate
from app.utils.security import hashPassword, verifyPassword, createToken

def createUser(userData: UserCreate, db: Session):
    getUser = db.query(User).filter(User.email == userData.email).first()
    if getUser:
        raise HTTPException(status_code=400, detail='Email already registered')

    hashedPassword = hashPassword(userData.password)

    newUser = User(
        name=userData.name,
        email=userData.email,
        password=hashedPassword,
        role=userData.role
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

def loginUser(loginData: UserLogin, db: Session):
    user = db.query(User).filter(User.email == loginData.email).first()
    if not user or not verifyPassword(loginData.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    
    token = createToken({'id': str(user.id), 'role': f'{user.role}'})
    return {'token': token}

def meUser(user: dict, db: Session):
    return user

def updateUser(userId: int, userData: UserUpdate, db: Session):
    user = db.query(User).filter(User.id == userId).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if userData.name is not None:
        user.name = userData.name
    if userData.email is not None:
        user.email = userData.email
    if userData.password is not None:
        user.password = hashPassword(userData.password)
    if userData.role is not None:
        user.role = userData.role

    db.commit()
    db.refresh(user)

    return user

def deleteUser(userId: int, db: Session):
    user = db.query(User).filter(User.id == userId).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    db.delete(user)
    db.commit()
    return {'message': 'User deleted.'}

def getUsers(id: Optional[int], name: Optional[str], email: Optional[str], db: Session):
    query = db.query(User)
    
    if name is not None:
        query = query.filter(User.name.ilike(f'%{name}%'))
    if email is not None:
        query = query.filter(User.email == email)
    if id is not None:
        query = query.filter(User.id == id)
    
    return query.all()