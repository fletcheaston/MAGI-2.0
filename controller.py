import pygame
import time
import sys


def init():
    global triggersPreviouslyPressed
    triggersPreviouslyPressed = set()


def getButtons(xbox_pad):
    allButtons = getButtonNames()
    pressedButtons = {
        "LB": 0,
        "RB": 0
    }

    pygame.event.get()
    for i in range(xbox_pad.get_numbuttons()):
        if(xbox_pad.get_button(i) == 1 and i in allButtons):
                if(allButtons[i] in pressedButtons):
                    pressedButtons[allButtons[i]] = 1
    
    return(pressedButtons)


def getTriggers(xbox_pad):
    allTriggers = getTriggerNames()
    pressedTriggers = {
        "RT": -1.0,
        "LT": -1.0
    }

    global triggersPreviouslyPressed
#    pygame.event.get()
    for i in range(xbox_pad.get_numaxes()):
        if(i in allTriggers):
            if(allTriggers[i] in triggersPreviouslyPressed or xbox_pad.get_axis(i) != 0):
                pressedTriggers[allTriggers[i]] = xbox_pad.get_axis(i)
                triggersPreviouslyPressed.add(allTriggers[i])

    return(pressedTriggers)


def getController():
    # Initialize PyGame for joystick functionality
    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    xbox_pad = joysticks[0]
    xbox_pad.init()
    time.sleep(1)
    return(xbox_pad)


def getButtonNames():
    buttonDict = {
        0: "A",
        1: "B",
        3: "X",
        4: "Y",
        6: "LB",
        7: "RB"
    }

    return(buttonDict)


def getTriggerNames():
    triggerDict = {
        4: "LT",
        5: "RT"
    }
    
    return(triggerDict)

