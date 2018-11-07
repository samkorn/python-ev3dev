#!/usr/bin/env python3
import sys
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sound import Sound


# initialize objects
sound = Sound()
right_motor = LargeMotor(OUTPUT_B)
left_motor = LargeMotor(OUTPUT_C)


# print test phrase to brick and computer
print("Hello my name is EV3!")                   # Display text on brick screen
print("Hello my name is EV3!", file=sys.stderr)  # Display text on computer


# go forward 2 rotations at speed 100
sound.speak("Moving forward two rotations")
right_motor.on_for_rotations(100, 2, block=False)
left_motor.on_for_rotations(100, 2, block=True)

# go forward 360 degrees at speed 100
sound.speak("Moving forward 360 degrees")
right_motor.on_for_degrees(100, 360, block=False)
left_motor.on_for_degrees(100, 360, block=True)

# go forward for 3 seconds at speed 100
sound.speak("Moving forward for three seconds")
right_motor.on_for_seconds(100, 3, block=False)
left_motor.on_for_seconds(100, 3, block=True)
