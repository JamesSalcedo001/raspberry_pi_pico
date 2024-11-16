# connect to wifi network
import network
import time
from secrets import SSID, PASSWORD
import urequests


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
else:
    print('Failed to connect.')

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

number = astronauts["number"]

for i in range(number):
    print(astronauts['people'][i]['name'])