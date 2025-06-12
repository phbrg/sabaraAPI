from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Query
from typing import Optional
from app.models.patient_model import Patient
from app.schemas.patient_schema import PatientCreate, PatientUpdate

def createPatient(patientData: PatientCreate, db: Session):
    getPatient = db.query(Patient).filter(Patient.cpf == patientData.cpf or Patient.email == patientData.email or Patient.phone == patientData.phone).first()
    if getPatient:
        raise HTTPException(status_code=400, detail='Patient alredy registered.')

    newPatient = Patient(
        full_name=patientData.full_name,
        birth_date=patientData.birth_date,
        cpf=patientData.cpf,
        phone=patientData.phone,
        email=patientData.email,
        allergies=patientData.allergies,
        notes=patientData.notes,
    )
    db.add(newPatient)
    db.commit()
    db.refresh(newPatient)

    return newPatient

def updatePatient(patientId: int, patientData: PatientUpdate, db: Session):
    patient = db.query(Patient).filter(Patient.id == patientId).first()
    if not patient:
        raise HTTPException(status_code=404, detail='Patient not found')

    if patientData.full_name is not None:
        patient.full_name = patientData.full_name
    if patientData.birth_date is not None:
        patient.birth_date = patientData.birth_date
    if patientData.cpf is not None:
        patient.cpf = patientData.cpf
    if patientData.phone is not None:
        patient.phone = patientData.phone
    if patientData.email is not None:
        patient.email = patientData.email
    if patientData.allergies is not None:
        patient.allergies = patientData.allergies
    if patientData.notes is not None:
        patient.notes = patientData.notes

    db.commit()
    db.refresh(patient)

    return patient

def deletePatient(patientId: int, db: Session):
    patient = db.query(Patient).filter(Patient.id == patientId).first()
    if not patient:
        raise HTTPException(status_code=404, detail='Patient not found')

    db.delete(patient)
    db.commit()
    return {'message': 'Patient deleted.'}

def getPatient(id: Optional[int], full_name: Optional[str], email: Optional[str], phone: Optional[str], cpf: Optional[str], db: Session):
    query = db.query(Patient)
    
    if id is not None:
      query = query.filter(Patient.id == id)
    if full_name is not None:
      query = query.filter(Patient.full_name.ilike(f'%{full_name}%'))
    if email is not None:
      query = query.filter(Patient.email == email)
    if phone is not None:
      query = query.filter(Patient.phone == phone)
    if cpf is not None:
      query = query.filter(Patient.cpf == cpf)
    
    return query.all()