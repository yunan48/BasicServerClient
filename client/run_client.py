import requests
import psutil
from time import sleep

TARGET_IP = "127.0.0.1"
API_URL = f"http://{TARGET_IP}:8000/cpu-monitor"

while True:
    sleep(2)
    cpu_usage = psutil.cpu_percent()

    payload = {"cpu_usage": cpu_usage}
    response = requests.post(API_URL, json=payload)

    print(f"Server response: {response.status_code}")

