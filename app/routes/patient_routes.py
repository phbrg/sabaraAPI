from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.connection import getDb
from app.schemas.patient_schema import PatientCreate, PatientOut, PatientUpdate
from app.utils.guards import getCurrentUser, isAdmin
from app.controllers.patient_controller import createPatient, updatePatient, deletePatient, getPatient

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

@router.post('/create', response_model=PatientOut)
def createPatientRoute(patientData: PatientCreate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return createPatient(patientData, db)

@router.put('/update/{patientId}', response_model=PatientOut)
def updatePatientRoute(patientId: int, patientData: PatientUpdate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return updatePatient(patientId, patientData, db)

@router.delete('/delete/{patientId}')
def deletePatientRoute(patientId: int, db: Session = Depends(getDb), user: dict = Depends(isAdmin)):
    return deletePatient(patientId, db)

@router.get('/', response_model=List[PatientOut])
def getPatientRoute(id: Optional[int] = Query(default=None), full_name: Optional[str] = Query(default=None), email: Optional[str] = Query(default=None), phone: Optional[str] = Query(default=None), cpf: Optional[str] = Query(default=None), db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return getPatient(id, full_name, email, phone, cpf, db)