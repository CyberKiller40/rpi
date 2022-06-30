
#!/usr/bin/env python3

from gpiozero import LightSensor,LED
from time import sleep

sens = LightSensor(4,charge_time_limit=0.03)
led = LED(17)

num = 0


while True:
    if sens.light_detected:
        led.off()
    else:
        led.on()
        num = num+1
        print(str(num)+" darkness!!!")

