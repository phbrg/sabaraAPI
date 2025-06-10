# from fastapi import Request
# from app.serial import serial

# arduinoData = serial.data

# def receiveData(current: bool=None):
#   if current:
#     return arduinoData[len(arduinoData)-1]
#   return arduinoData

# A FAZER: ROTA DE ENVIAR COMANDOS AO ARDUINO
# def sendCommand(command: str):
#     return serial.sendCommand(command)