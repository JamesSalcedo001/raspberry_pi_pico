# connect to wifi network
import network
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Wi-Fi credentials from environment variables
SSID = os.getenv("SSID")
PASSWORD = os.getenv("PASSWORD")

# create an object to create connection from code to Pico wireless chip
wlan = network.WLAN(network.STA_IF)

# turn on raspberry pi pico w's wifi
wlan.active(True)

# connect to router using env variables
wlan.connect(SSID, PASSWORD)

# Check and print connection status
max_wait = 15
while max_wait > 0:
    if wlan.isconnected():
        break
    print('waiting for connection...')
    time.sleep(1)
    max_wait -= 1

if wlan.isconnected():
    print('Connected successfully!')
    print('Network configuration:', wlan.ifconfig())
else:
    print('Failed to connect.')
