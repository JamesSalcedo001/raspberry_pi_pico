# connect to wifi network
import network

# add a pause to code
import time


# create an object to create connection from code to Pico wireless chip


# use this to connect and check wifi connection
wlan = network.WLAN(network.STA_IF)

# turn on raspberry pi pico w's wifi
wlan.active(True)


