#!/usr/bin/env python3
import sys
import evdev
import threading

from ev3dev2.motor import LargeMotor, MediumMotor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D


## Helper functions ##

# ensure that the motor is only passed values in the range (-1000, 1000)
def clamp(val):
    # TODO: Fill this in!
    pass

# scale the value from the source range to the destination range
def scale(val, src, dst):
    # TODO: Fill this in!
    pass


## Initializing ##
print("Finding ps3 controller...", file=sys.stderr)
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == 'PLAYSTATION(R)3 Controller':
        ps3 = device.fn
gamepad = evdev.InputDevice(ps3)


## Set up variables ##
running = True
# TODO: Set initial speed variables to zero


## Motor thread class ##
class MotorThread(threading.Thread):
    def __init__(self):
        # TODO: Initialize motors
        threading.Thread.__init__(self)

    def run(self):
        print("Engine running!", file=sys.stderr)
        while running:
            # TODO: Set motors to run at speed determined by remote
            pass
        # TODO: Stop motors


## MAIN PROGRAM ##

# start the motor thread
motor_thread = MotorThread()        # creates a new motor thread
motor_thread.setDaemon(True)        # makes the thread a "daemon" thread
motor_thread.start()                # starts the thread

# loop infinitely, setting speeds based on event codes
for event in gamepad.read_loop():   # this makes it loop infinitely
    # TODO: Set speed variables based on event code input

    # If the "X" button is pressed, stop the robot and end the program
    if event.type == 1 and event.code == 304 and event.value == 1:
        print("X button is pressed. Stopping.", file=sys.stderr)
        running = False
        break
