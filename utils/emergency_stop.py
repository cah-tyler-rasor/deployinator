#!/usr/bin/env python3

import os
from gpiozero import Button
from signal import pause

def reboot_the_thing():
  os.system('sudo reboot')

emergency_stop = Button(16)
emergency_stop.when_pressed = reboot_the_thing

pause()
