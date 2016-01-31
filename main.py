#!/usr/bin/env python3

from time import sleep
from utils.mqtt import publish
from weather import Weather

w = Weather()

while True:
    publish(w.basics(),"stormfly")
    sleep(600)
    w.refresh()
