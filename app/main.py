from fastapi import FastAPI
from app.routes import arduino_routes
from app.serial.serial import startSerial

app = FastAPI()
startSerial()
app.include_router(arduino_routes.router, prefix="", tags=["Arduino"])