import paho.mqtt.client as mqtt
import requests

API_URL = 'http://127.0.0.1:8000/room/create'

sensor_data = {
    'temperature': None,
    'humidity': None,
    'light': None
}

def sendData():
    if None not in sensor_data.values():
        print('Sending data to API:', sensor_data)
        try:
            response = requests.post(API_URL, json=sensor_data)
            print('API Response:', response.status_code, response.text)
        except Exception as e:
            print('Send data error:', e)

def onConnect(client, userdata, flags, rc):
    print(f'Broker successfully connected: {rc}')
    client.subscribe('sensor/temperature')
    client.subscribe('sensor/humidity')
    client.subscribe('sensor/light')

def onMessage(client, userdata, msg):
    topic_map = {
        'sensor/temperature': 'temperature',
        'sensor/humidity': 'humidity',
        'sensor/light': 'light',
    }

    topic = msg.topic
    payload = msg.payload.decode('utf-8')

    if topic in topic_map:
        key = topic_map[topic]
        try:
            sensor_data[key] = float(payload)
            print(f'{key}: {sensor_data[key]}')
            sendData()
        except ValueError:
            print(f'Invalid value received: {key}: {payload}')

client = mqtt.Client()
client.on_connect = onConnect
client.on_message = onMessage

client.connect('broker.hivemq.com', 1883, 60)

print('Awaiting messages...')
client.loop_forever()