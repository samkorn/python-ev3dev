#!/usr/bin/env python3
import evdev
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D

## Initialize controller ##
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == "PLAYSTATION(R)3 Controller":
        ps3 = device.fn
gamepad = evdev.InputDevice(ps3)


## Initialize motors ##
# TODO: FILL IN (see commented example below)
# motor = MediumMotor(OUTPUT_A)


# loop infinitely until the user presses some button
for event in gamepad.read_loop():
    t = None    # TODO: FILL IN
    c = None    # TODO: FILL IN
    v = None    # TODO: FILL IN
    if event.type == t and event.code == c and event.value == v:
        # TODO: Give the bot an action, then stop (see commented example below)
        # motor.on_for_rotations(75, 3)
        break       # this breaks the loop, and ends the program
