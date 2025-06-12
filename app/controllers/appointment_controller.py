from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status, Query
from typing import Optional
from datetime import datetime
from app.models.appointment_model import Appointment
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdate

def createAppointment(appointmentData: AppointmentCreate, db: Session):
    appointmentDate = datetime.strptime(appointmentData.date, "%d-%m-%Y")

    newAppointment = Appointment(
        patient_id=appointmentData.patient_id,
        patient_name=appointmentData.patient_name,
        medic_id=appointmentData.medic_id,
        medic_name=appointmentData.medic_name,
        date=appointmentDate,
        appointmentType=appointmentData.appointmentType
    )
    db.add(newAppointment)
    db.commit()
    db.refresh(newAppointment)

    return newAppointment

def updateAppointment(appointmentId: int, appointmentData: AppointmentUpdate, db: Session):
    appointment = db.query(Appointment).filter(Appointment.id == appointmentId).first()
    if not appointment:
        raise HTTPException(status_code=404, detail='Appointment not found')

    if appointmentData.date is not None:
        birthDate = datetime.strptime(appointmentData.date, "%d-%m-%Y")
        appointment.date = birthDate
    if appointmentData.medic_id is not None:
        appointment.medic_id = appointmentData.medic_id
    if appointmentData.patient_id is not None:
        appointment.patient_id = appointmentData.patient_id
    if appointmentData.appointmentType is not None:
        appointment.appointmentType = appointmentData.appointmentType
    if appointmentData.medic_name is not None:
        appointment.medic_name = appointmentData.medic_name
    if appointmentData.patient_name is not None:
        appointment.patient_name = appointmentData.patient_name

    db.commit()
    db.refresh(appointment)

    return appointment
  
def deleteAppointment(appointmentId: int, db: Session):
    appointment = db.query(Appointment).filter(Appointment.id == appointmentId).first()
    if not appointment:
        raise HTTPException(status_code=404, detail='Appointment not found')

    db.delete(appointment)
    db.commit()
    return {'message': 'Appointment deleted.'}

def getAppointment(id: Optional[int], medic_id: Optional[int], medic_name: Optional[str], patient_id: Optional[int], patient_name: Optional[str], db: Session):
    query = db.query(Appointment)
    
    if id is not None:
      query = query.filter(Appointment.id == id)
    if medic_id is not None:
      query = query.filter(Appointment.medic_id == medic_id)
    if medic_name is not None:
      query = query.filter(Appointment.medic_name.ilike(f'%{medic_name}%'))
    if patient_name is not None:
      query = query.filter(Appointment.patient_name.ilike(f'%{patient_name}%'))
    if patient_id is not None:
      query = query.filter(Appointment.patient_id == patient_id)
    
    return query.all()
