#!/usr/bin/env python3

from ckgpio import disp7seg
from time import sleep
import threading

rdisp = disp7seg(17,4,23,25,6,27,24,18,False)
ldisp = disp7seg(13,22,12,16,20,26,19,5,False)

def hexcounter():
    number = 0
    rdisp.alloff()
    ldisp.alloff()
    try:
        while True:
            num = list(format(number, '02x'))
            print("number = " + str(number) + " hex = " + str(num))
            rdisp.shownum(num[1])
            ldisp.shownum(num[0])
            if number < 255: number+=1
            else: number = 0
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nCounter end")
        rdisp.alloff()
        ldisp.alloff()

def deccounter():
    number = 0
    rdisp.alloff()
    ldisp.alloff()
    try:
        while True:
            num = list(format(number, '02'))
            print("number = " + str(number))
            rdisp.shownum(num[1])
            ldisp.shownum(num[0])
            if number < 99: number+=1
            else: number = 0
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nCounter end")
        rdisp.alloff()
        ldisp.alloff()

def blinker():
    ldisp.segdot.on()
    rdisp.segdot.off()
    try:
        while True:
            ldisp.segdot.toggle()
            rdisp.segdot.toggle()
            sleep(0.5)
    except KeyboardInterrupt:
        print("\nBack to menu")
        ldisp.segdot.off()
        rdisp.segdot.off()

def anim1():
    rdisp.alloff()
    ldisp.alloff()
    try:
        rdisp.segdot.on()
        sleep(0.5)
        rdisp.segdot.off()
        while True:
            rdisp.segc.off()
            rdisp.segd.on()
            sleep(0.1)
            rdisp.segd.off()
            ldisp.segdot.on()
            sleep(0.1)
            ldisp.segdot.off()
            ldisp.segd.on()
            sleep(0.1)
            ldisp.segd.off()
            ldisp.sege.on()
            sleep(0.1)
            ldisp.sege.off()
            ldisp.segf.on()
            sleep(0.1)
            ldisp.segf.off()
            ldisp.sega.on()
            sleep(0.1)
            ldisp.sega.off()
            rdisp.sega.on()
            sleep(0.1)
            rdisp.sega.off()
            rdisp.segb.on()
            sleep(0.1)
            rdisp.segb.off()
            rdisp.segc.on()
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimation 1 end")
        rdisp.alloff()
        ldisp.alloff()

def anim2():
    rdisp.alloff()
    ldisp.alloff()
    try:
        rdisp.segg.on()
        ldisp.segg.on()
        sleep(0.5)
        rdisp.segg.off()
        ldisp.segg.off()
        while True:
            rdisp.segc.off()
            ldisp.sege.off()
            rdisp.segb.on()
            ldisp.segf.on()
            sleep(0.1)
            rdisp.segb.off()
            ldisp.segf.off()
            rdisp.sega.on()
            ldisp.sega.on()
            sleep(0.1)
            rdisp.sega.off()
            ldisp.sega.off()
            rdisp.segf.on()
            ldisp.segb.on()
            sleep(0.1)
            rdisp.segf.off()
            ldisp.segb.off()
            rdisp.sege.on()
            ldisp.segc.on()
            sleep(0.1)
            rdisp.sege.off()
            ldisp.segc.off()
            rdisp.segd.on()
            ldisp.segd.on()
            sleep(0.1)
            rdisp.segd.off()
            ldisp.segd.off()
            rdisp.segc.on()
            ldisp.sege.on()
            sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimation 2 end")
        rdisp.alloff()
        ldisp.alloff()


#bgblink = threading.Thread(target=blinker,daemon=True)
#bgblink.start()

while True:
    print("\n-------------------------------------------------------\n\n")
    print("Menu:\n1. hexcounter\n2. deccounter\n3. blinker\n4. anim 1\n5. anim 2\n6. quit")
    menu=input()
    if menu=="1":
        print("\nCounter starting...\n")
        hexcounter()
    elif menu=="2":
        print("\nCounter starting...\n")
        deccounter()
    elif menu=="3":
        print("\nBlinker")
        blinker()
    elif menu=="4":
        print("\nAnimation 1")
        anim1()
    elif menu=="5":
        print("\nAnimation 2")
        anim2()
    elif menu=="6":
        print("\nQuitting...")
        quit()
    else:
        print("\nWrong entry")
        input("Press enter") 

