#!/usr/bin/env python3

from gpiozero import LED
from time import sleep

led1 = LED(23)
led2 = LED(17)
led4 = LED(27)
led8 = LED(22)

number = 0
while True:
    num = list(str("{0:04b}".format(number)))
    print("number = " + str(number) + " bin = " + str(num))
    if num[3] == '1':
        led1.on()
    else:
        led1.off()
    if num[2] == '1':
        led2.on()
    else:
        led2.off()
    if num[1] == '1':
        led4.on()
    else:
        led4.off()
    if num[0] == '1':
        led8.on()
    else:
        led8.off()
    if number < 15:
        number = number + 1
    else:
        number = 0
    sleep(0.5)


