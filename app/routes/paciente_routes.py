# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.db.connection import SessionLocal
# from app.controllers import paciente_controller
# from app.schemas.paciente_schema import PacienteCreate

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/")
# def list_pacientes(db: Session = Depends(get_db)):
#     return paciente_controller.get_all_pacientes(db)

# @router.get("/{paciente_id}")
# def get_paciente(paciente_id: int, db: Session = Depends(get_db)):
#     paciente = paciente_controller.get_paciente_by_id(db, paciente_id)
#     if not paciente:
#         raise HTTPException(status_code=404, detail="paciente não encontrado")
#     return paciente

# @router.post("/")
# def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
#     return paciente_controller.create_paciente(db, paciente.name, paciente.idade, paciente.caso)

# @router.delete("/{paciente_id}")
# def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
#     paciente = paciente_controller.delete_paciente(db, paciente_id)
#     if not paciente:
#         raise HTTPException(status_code=404, detail="paciente não encontrado")
#     return {"message": "paciente deletado com sucesso"}