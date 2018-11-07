#!/usr/bin/env python3
import evdev
import sys


# initialize controller
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == "PLAYSTATION(R)3 Controller":
        ps3 = device.fn
gamepad = evdev.InputDevice(ps3)


print("STARTING LOOP.", file=sys.stderr)
for event in gamepad.read_loop():
    # comment out to declutter
    print(event.type, event.code, event.value, file=sys.stderr)

    # uncomment to see events
    # if event.type == 3 and event.code == 3:
    #     print(event.value, file=sys.stderr)
