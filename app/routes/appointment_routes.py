from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional, List
from app.db.connection import getDb
from app.schemas.appointment_schema import AppointmentCreate, AppointmentOut, AppointmentUpdate
from app.utils.guards import getCurrentUser, isAdmin
from app.controllers.appointment_controller import createAppointment, updateAppointment, deleteAppointment, getAppointment

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

@router.post('/create', response_model=AppointmentOut)
def createAppointmentRoute(appointmentData: AppointmentCreate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return createAppointment(appointmentData, db)

@router.put('/update/{appointmentId}', response_model=AppointmentOut)
def updateAppointmentRoute(appointmentId: int, appointmentData: AppointmentUpdate, db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return updateAppointment(appointmentId, appointmentData, db)

@router.delete('/delete/{appointmentId}')
def deleteAppointmentRoute(appointmentId: int, db: Session = Depends(getDb), user: dict = Depends(isAdmin)):
    return deleteAppointment(appointmentId, db)

@router.get('/', response_model=List[AppointmentOut])
def getAppointmentRoute(id: Optional[int] = Query(default=None), medic_id: Optional[int] = Query(default=None), patient_id: Optional[int] = Query(default=None), db: Session = Depends(getDb), user: dict = Depends(getCurrentUser)):
    return getAppointment(id, medic_id, patient_id, db)