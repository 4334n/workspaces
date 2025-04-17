import serial
import time

def toggle_led():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600)
        time.sleep(2)  # Let the serial connection settle
        ser.write(b'1')  # Turn LED on
        print('LED ON')
        time.sleep(5)
        ser.write(b'0')  # Turn LED off
        print('LED OFF')
        ser.close()
    except serial.SerialException as e:
        print(f"Serial error: {e}")
