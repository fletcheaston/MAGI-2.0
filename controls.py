# Created by Fletcher Easton

import serial;

def keepInRange(num, min_num, max_num):
    return(min(max(num, min_num), max_num))


def setMotorSpeed(motorSerial, leftSpeed, rightSpeed):
    leftSpeed = keepInRange(leftSpeed, -250, 250)
    rightSpeed = keepInRange(rightSpeed, -250, 250)
    serialString = "{0} {1}\n".format(leftSpeed, rightSpeed)
    writeSerialString(motorSerial, serialString)


# Utility method to write data to the robot.
def writeSerialString(motorSerial, string):
    bytes = string.encode()
    motorSerial.write(bytes)
