from sqlalchemy.orm import Session
from app.models.paciente_model import Paciente

def get_all_pacientes(db: Session):
    return db.query(Paciente).all()

def get_paciente_by_id(db: Session, paciente_id: int):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def create_paciente(db: Session, name: str, idade: int, caso: str):
    new_paciente = Paciente(name=name, idade=idade, caso=caso)
    db.add(new_paciente)
    db.commit()
    db.refresh(new_paciente)
    return new_paciente

def delete_paciente(db: Session, paciente_id: int):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if paciente:
        db.delete(paciente)
        db.commit()
    return paciente
