import serial
import threading

data = []

def readSerial():
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
        with open('room.log', 'a') as log:
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    data.append(line)
                    log.write(f'{line}\n')
                    log.flush()
    except Exception as e:
        print(f'Serial Error: {e}')

# def sendCommand(command: str):
#     try:
#         with serial.Serial('COM3', 9600, timeout=1) as ser:
#             ser.write(f'{command}\n'.encode())
#             return f'OK: {command}'
#     except Exception as e:
#         print(f'Command Error: {e}')
#         return f'Command Error: {e}'

def startSerial():
    thread = threading.Thread(target=readSerial)
    thread.daemon = True
    thread.start()