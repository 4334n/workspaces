from sensors.dht import read_and_send_dht_data
from control.led_control import toggle_led
from camera.stream import run_stream_server

if __name__ == "__main__":
    # You can uncomment one at a time for testing
    read_and_send_dht_data()
    # toggle_led()
    # run_stream_server()
