# connect to wifi network
import network
import time

# import urequests module, enables one to work with network requests such as HTTP and JSON
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

# create astronaut object and use urequests to get info in JSON format
astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

# create object, number which will open astronauts object and look for the key "number", the value linked to the key is then stored in the number object
number = astronauts["number"]

# create loop that iterates for the number of people on the international space station
for i in range(number):
    # print name of each astronaut on the International space station using a series of keys that target the specific data
    print(astronauts['people'][i]['name'])
    # i increments every time the loop repeats and selects each person from the list of embedded data, then use "name" key to access the name values of each