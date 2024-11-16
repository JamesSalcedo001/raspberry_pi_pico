# connect to wifi network
import network

# add a pause to code
import time

import os

from dotenv import load_dotenv


# load environment variables
load_dotenv()

# retrieve wifi credentials from .env

SSID = os.getenv("SSID")
PASSWORD = os.getenv("PASSWORD")


# create an object to create connection from code to Pico wireless chip


# use this to connect and check wifi connection
wlan = network.WLAN(network.STA_IF)

# turn on raspberry pi pico w's wifi
wlan.active(True)


# connect to router using env variables
wlan.connect(SSID, PASSWORD)

print(wlan.isconnected())