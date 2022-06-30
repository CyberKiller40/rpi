#!/usr/bin/env python3

from gpiozero import TrafficLights
from time import sleep

traf = TrafficLights(27,17,4)

#traf.blink(background=False)
while True:
    traf.red.on()
    sleep(5)
    traf.amber.on()
    sleep(2)
    traf.toggle()
    sleep(5)
    traf.green.off()
    traf.amber.on()
    sleep(2)
    traf.amber.off()
