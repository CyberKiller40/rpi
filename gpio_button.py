#!/usr/bin/env python3

from gpiozero import Button
from time import sleep

button = Button(2)

while True:
    button.wait_for_press()
    print("pushed")
    sleep(1)

