# Created by Fletcher Easton

import controller
import controls
import serial
import time
import sys


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return(rightMin + (valueScaled * rightSpan))


if __name__ == '__main__':
    controller.init()
    motorSerial = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
    xbox = controller.getController()
    
    while(True):
        leftSpeed = 0
        rightSpeed = 0
        
        buttons = controller.getButtons(xbox)
        triggers = controller.getTriggers(xbox)
        
        leftSpeed = translate(triggers["LT"], -1, 1, -250, 250)
        rightSpeed = translate(triggers["RT"], -1, 1, -250, 250)
        
        if(buttons["LB"] == 1):
            leftSpeed *= 1.5
            rightSpeed /= 1.5
    
        if(buttons["RB"] == 1):
            leftSpeed /= 1.5
            rightSpeed *= 1.5
        
        print(leftSpeed, rightSpeed)

        controls.setMotorSpeed(motorSerial, leftSpeed, rightSpeed)
