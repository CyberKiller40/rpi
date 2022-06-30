#!/usr/bin/env python3

import smbus
from time import sleep


bus = smbus.SMBus(1)
addr = 0x50

def readchip():
    oldstr=""
    for i in range(0x00,0xff):
        oldstr=oldstr+chr(bus.read_byte_data(addr,i))
    return oldstr
    
def writechip(newstr):
    if len(newstr)>256:
        print("String too long, max is 256 chars")
        return
    else:
        tmpstr=""
        for i in range(0,len(newstr)):
            if ord(newstr[i])>=255:
                tmpstr+="-"
            else:
                tmpstr+=newstr[i]
            #print(str(i) + " " + newstr[i] + " " + str(ord(newstr[i])))
            bus.write_byte_data(addr,int(i),ord(tmpstr[i]))
            sleep(0.1)
        print("Written")
        return

while True:
    print("\n-------------------------------------------------------\n\nMenu:\n1. read\n2. write\n3. quit")
    menu=input()
    if menu=="1":
        print("\nReading:\n" + readchip())
        input() 
    elif menu=="2":
        mess=input("\nEnter message: ")
        print("Writing...")
        writechip(mess)
        input() 
    elif menu=="3":
        print("\nQuitting...")
        quit()
    else:
        print("\nWrong entry")
        input() 


