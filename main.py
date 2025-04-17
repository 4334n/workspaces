from sensors.dht import read_and_send_dht_data
from control.led_control import toggle_led
from camera.stream import run_stream_server

# Example usage
if __name__ == "__main__":
    read_and_send_dht_data()
    # toggle_led()
    # run_stream_server()

import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed, RequestError

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Update with your actual GPIO pin

ADA_FRUIT_KEY = 'YOUR_AIO_KEY'
aio = Client(ADA_FRUIT_KEY)

def read_and_send_dht_data():
    try:
        aio.create_feed(Feed(name='temperature'))
    except RequestError:
        pass
    try:
        aio.create_feed(Feed(name='humidity'))
    except RequestError:
        pass

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f'Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%')
            aio.send('temperature', temperature)
            aio.send('humidity', humidity)
        else:
            print("Sensor failure.")
        time.sleep(60)

import serial
import time

def toggle_led():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    time.sleep(2)
    ser.write(b'1')
    print('LED ON')
    time.sleep(5)
    ser.write(b'0')
    print('LED OFF')
    ser.close()

from flask import Flask, Response
from picamera import PiCamera

app = Flask(__name__)
camera = PiCamera()

@app.route('/stream')
def stream():
    return Response(camera.capture_continuous('/tmp/image.jpg'), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '<h1>Camera Stream</h1><img src="/stream" />'

def run_stream_server():
    app.run(host='0.0.0.0', port=5000)

