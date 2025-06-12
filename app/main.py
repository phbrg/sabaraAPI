from fastapi import FastAPI
from app.routes import user_routes, patient_routes

app = FastAPI()
app.include_router(user_routes.router, prefix='/user', tags=['Users'])
app.include_router(patient_routes.router, prefix='/patient', tags=['Patients'])