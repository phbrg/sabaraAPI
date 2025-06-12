from sqlalchemy import Column, Integer, String, Enum, DateTime
from datetime import datetime
from app.db.connection import Base
import enum

class RoleEnum(enum.Enum):
    MEDICO = 'medico'
    RECEPCAO = 'recepcao'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)