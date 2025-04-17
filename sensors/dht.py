import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed, RequestError

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Adjust to your GPIO pin
ADA_FRUIT_KEY = 'YOUR_AIO_KEY'  # Replace with your actual key

aio = Client(ADA_FRUIT_KEY)

def read_and_send_dht_data():
    for feed_name in ['temperature', 'humidity']:
        try:
            aio.create_feed(Feed(name=feed_name))
        except RequestError:
            pass  # Feed already exists

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f'Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%')
            aio.send('temperature', temperature)
            aio.send('humidity', humidity)
        else:
            print("Sensor read failed.")
        time.sleep(60)
