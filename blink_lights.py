#!/usr/bin/python3

from gpiozero import LED, Button
from signal import pause

led = LED(23)
key = Button(24)

key.when_pressed = led.blink()
key.when_released = led.off

pause()
