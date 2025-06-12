from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from app.utils.security import decodeToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

def getCurrentUser(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = decodeToken(token)
        userId = payload.get('id')
        role = payload.get('role')

        if not userId or not role:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access denied.')

        return {'id': userId, 'role': role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access denied.')

def isAdmin(token: str = Depends(oauth2_scheme)) -> bool:
    user = getCurrentUser(token)
    
    if user['role'] == 'RoleEnum.ADMIN':
        return user
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Access denied.')