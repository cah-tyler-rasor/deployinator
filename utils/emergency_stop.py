#!/usr/bin/env python3

import os
from gpiozero import Button, LED
from signal import pause
import time

def alert_shutdown_about_to_happen():
  led = LED(23)
  for _ in range(10):
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

def reboot_the_thing():
  alert_shutdown_about_to_happen()
  os.system('sudo reboot')

emergency_stop = Button(16)
emergency_stop.when_pressed = reboot_the_thing

pause()
