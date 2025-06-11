from app.db.connection import Base, engine
from app.models.user_model import User
from app.models.patient_model import Patient
from app.models.room_model import Room
from app.models.prontuario_model import Prontuario
from app.models.appointment_model import Appointment

Base.metadata.create_all(bind=engine)