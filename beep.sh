#!/bin/bash

#beep script

PIN=18
PWMVAL=20
#PWMVAL is 0-1023
BEEPTIME=0.25

#-------------------------------

gpio -g mode $PIN pwm
gpio -g pwm $PIN $PWMVAL 

#to turn on
gpio pwm-ms
sleep $BEEPTIME
#to turn off
gpio -g mode $PIN in

