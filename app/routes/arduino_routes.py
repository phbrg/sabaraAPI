# from fastapi import APIRouter, Request
# from app.controllers import arduino_controller
# from typing import Optional

# router = APIRouter()

# @router.get('/data/')
# def receiveDataFromArduino(current: Optional[bool] = None):
#     if current:
#         return arduino_controller.receiveData(True)
#     return arduino_controller.receiveData()

# A FAZER: ROTA DE ENVIAR COMANDOS AO ARDUINO
# @router.post('/send')
# def sendCommandToArduino(command: dict):
#     print(command)
#     return arduino_controller.sendCommand(command)