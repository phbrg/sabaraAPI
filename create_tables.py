from app.db.connection import Base, engine
from app.models.paciente_model import Paciente

Base.metadata.create_all(bind=engine)