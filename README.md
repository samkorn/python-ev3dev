# python-ev3dev #
## Python ev3dev + PS3 Remote Control Tutorial ##

This repository contains the basic code necessary to create your very own PS3-controlled EV3 Robot!

### DIRECTORY LAYOUT ###
```bash
.
|—— .vscode/             # Visual Studio Code Settings (don't mess with these!)
|    |—— launch.json
|    |—— settings.json
|—— python-tutorials/    # Beginner python tutorials
|    |—— classes.py      # Python classes tutorial (3rd)
|    |—— functions.py    # Python functions tutorial (2nd)
|    |—— hello.py        # Very first program! (1st)
|—— basic_remote.py      # Basic PS3 remote control
|—— ev3_demo.py          # A demo of the EV3 motors
|—— ps3_test.py          # Testing sandbox for the PS3 interface
|—— ps3-map.txt          # PS3 evdev event code map
|—— remote.py            # Final remote control program
```

### Installation ###
The following instructions assume that the user is working with Mac OS 10.

In order to use this workflow, you must have VSCode installed. You will need to install two additional extensions:
-Python (2018.9.2+)
-ev3dev-browser (0.8.1+)
These can be installed from the extensions button on the left sidebar of VSCode. Once installed, you will need to reload VSCode.


## Running ev3dev Scripts ##

### Pairing your PS3 Remote with your EV3 ###
1) First make sure that bluetooth is Visible and Powered On on your brick. This should be under 'Wireless and Networks > Bluetooth'.
2) Connect the controller to your brick via a USB and/or mini-USB cable.
3) Under 'Wireless and Networks > Bluetooth > Devices' a new device should appear labelled "PLAYSTATION(R) 3 controller".
4) Disconnect the USB cable from both ends.
5) Press the PlayStation button on the controller.
6) The brick will ask "Authorize service HID?" Press 'Accept'.

### Connecting your PS3 Remote to your EV3 ###
1) Press the PlayStation button on the controller.
2) The brick will ask "Authorize service HID?" Press 'Accept'.

### Pairing your EV3 with your Computer ###
1) In order to pair your EV3, first make sure that bluetooth is Visible and Powered On on your brick. This should be under 'Wireless and Networks > Bluetooth'.
2) On your computer, go to 'System Preferences > Bluetooth' and turn Bluetooth on if it isn't already.
3) A device labeled "ev3dev" should appear on the screen, with a button to the right labeled "pair". Select this button.
4) A numerical code should appear on both the computer and on the brick. Press 'Accept' on the brick. You should now be paired.

### Connecting your EV3 to your Computer ###
1) On your computer, go to 'System Preferences > Bluetooth' and turn Bluetooh on if it isn't already.
2) Double click on the device labeled "ev3dev".
3) A prompt should pop up on your brick asking if you want to "Authorize Service BNEP?". Press 'Accept'.

### Connecting your EV3 to VS Code ###
1) In Visual Studio Code, under the sidebar menu labeled "EV3DEV DEVICE BROWSER", select the option that says "Click here to connect to a device".
2) Select the ev3dev device from the dropdown menu. If you've connected succesfully, your device should appear in the device browser, with a small green circle next to it. See Troubleshooting for problem solving steps if this does not work. 

### Running a script using the VS Code ev3dev Workflow ###
1) Once you've written a script and saved it, and you've connected your EV3 to the VS Code browser, you should be able to remotely run scripts on your brick from your computer. In order to remotely run a script, simply by pressing the F5 key (or fn + F5) on your keyboard.
2) Be patient!! Connecting to the brick, and then importing modules takes a long time with this workflow. It is a good idea to include a sound file or print statement after the import statements in your code so that you know the program is ready to run.
