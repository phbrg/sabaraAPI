from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

pwdContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hashPassword(password: str) -> str:
  return pwdContext.hash(password)

def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
  return pwdContext.verify(plainPassword, hashedPassword)

def createToken(data: dict) -> str:
  toEncode = data.copy()
  date = datetime.utcnow() + timedelta(days=7)
  toEncode.update({'exp': date})
  return jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)

def decodeToken(token: str) -> dict:
  return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])