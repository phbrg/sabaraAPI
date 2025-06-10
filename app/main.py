from fastapi import FastAPI
from app.routes import paciente_routes

app = FastAPI()
app.include_router(paciente_routes.router, prefix="", tags=["paciente"])