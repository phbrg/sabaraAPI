from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status, Query
from typing import Optional
from datetime import datetime
from app.models.prontuario_model import Prontuario, StatusEnum
from app.schemas.prontuario_schema import ProntuarioCreate, ProntuarioUpdate

def createProntuario(prontuarioData: ProntuarioCreate, db: Session):
    newProntuario = Prontuario(
        patient_id=prontuarioData.patient_id,
        patient_name=prontuarioData.patient_name,
        medic_id=prontuarioData.medic_id,
        medic_name=prontuarioData.medic_name,
        description=prontuarioData.description,
        status=StatusEnum.PENDENTE
    )
    db.add(newProntuario)
    db.commit()
    db.refresh(newProntuario)

    return newProntuario

def updateProntuario(prontuarioId: int, prontuarioData: ProntuarioUpdate, db: Session):
    prontuario = db.query(Prontuario).filter(Prontuario.id == prontuarioId).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail='Prontuario not found')

    if prontuarioData.medic_id is not None:
        prontuario.medic_id = prontuarioData.medic_id
    if prontuarioData.patient_id is not None:
        prontuario.patient_id = prontuarioData.patient_id
    if prontuarioData.medic_name is not None:
        prontuario.medic_name = prontuarioData.medic_name
    if prontuarioData.patient_name is not None:
        prontuario.patient_name = prontuarioData.patient_name
    if prontuarioData.description is not None:
        prontuario.description = prontuarioData.description
    if prontuarioData.status is not None:
        prontuario.status = prontuarioData.status

    db.commit()
    db.refresh(prontuario)

    return prontuario
  
def deleteProntuario(prontuarioId: int, db: Session):
    prontuario = db.query(Prontuario).filter(Prontuario.id == prontuarioId).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail='Prontuario not found')

    db.delete(prontuario)
    db.commit()
    return {'message': 'Prontuario deleted.'}

def getProntuario(id: Optional[int], medic_id: Optional[int], medic_name: Optional[str], patient_id: Optional[int], patient_name: Optional[str], db: Session):
    query = db.query(Prontuario)
    
    if id is not None:
      query = query.filter(Prontuario.id == id)
    if medic_id is not None:
      query = query.filter(Prontuario.medic_id == medic_id)
    if medic_name is not None:
      query = query.filter(Prontuario.medic_name.ilike(f'%{medic_name}%'))
    if patient_name is not None:
      query = query.filter(Prontuario.patient_name.ilike(f'%{patient_name}%'))
    if patient_id is not None:
      query = query.filter(Prontuario.patient_id == patient_id)
    
    return query.all()