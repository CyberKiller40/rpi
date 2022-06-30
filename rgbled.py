#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

myled = RGBLED(17, 27, 22, False)
myled.blink(1,1,1,1,(0.5,0,1),(0.5,1,0),10,False)

