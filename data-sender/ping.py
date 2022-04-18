import json
import requests
import serial
import time
from datetime import datetime


URL = "http://87.92.222.33:8976/"


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            timestamp = datetime.utcnow().strftime('%H:%M:%S - %b %d %Y')
            r = requests.post(url = URL, json = {'device_name': 'SENSOR 1', 'data': line, 'time_utc': timestamp})
            time.sleep(60)
