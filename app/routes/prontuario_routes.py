from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.connection import getDb
from app.schemas.prontuario_schema import ProntuarioCreate, ProntuarioOut, ProntuarioUpdate
from app.utils.guards import getCurrentUser, isAdmin
from app.controllers.prontuario_controller import createProntuario, updateProntuario, deleteProntuario, getProntuario

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

@router.post('/create', response_model=ProntuarioOut)
def createProntuarioRoute(prontuarioData: ProntuarioCreate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return createProntuario(prontuarioData, db)

@router.put('/update/{prontuarioId}', response_model=ProntuarioOut)
def updateProntuarioRoute(prontuarioId: int, prontuarioData: ProntuarioUpdate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return updateProntuario(prontuarioId, prontuarioData, db)

@router.delete('/delete/{prontuarioId}')
def deleteProntuarioRoute(prontuarioId: int, db: Session = Depends(getDb), user: dict = Depends(isAdmin)):
    return deleteProntuario(prontuarioId, db)

@router.get('/', response_model=List[ProntuarioOut])
def getProntuarioRoute(id: Optional[int] = Query(default=None), medic_id: Optional[int] = Query(default=None), medic_name: Optional[str] = Query(default=None), patient_id: Optional[int] = Query(default=None), patient_name: Optional[str] = Query(default=None), db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return getProntuario(id, medic_id, medic_name, patient_id, patient_name, db)