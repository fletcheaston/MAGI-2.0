# Created by Fletcher Easton

import controller
import controls
import serial
import time
import sys

if __name__ == '__main__':
    controller.init()
#    motorSerial = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
    xbox = controller.getController()
    
    while(True):
        print(controller.getButtons(xbox))
        print(controller.getTriggers(xbox))
        time.sleep(0.5)

    while(True):
        speeds = input("Enter Speeds: ").split(" ")

        if(speeds[0] == "quit"):
            sys.exit(0)
        
        if(len(speeds) != 2):
            print("Error: Incorrect number of speeds given.")
        else:
            try:
                leftSpeed = int(speeds[0])
                rightSpeed = int(speeds[1])
                controls.setMotorSpeed(motorSerial, leftSpeed, rightSpeed)
            except:
                print("Error: Unable to parse speeds given.")

        time.sleep(0.5)
