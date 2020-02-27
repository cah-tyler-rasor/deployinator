#!/usr/bin/env python3

from gpiozero import LED
import time

led = LED(23)

for _ in range(3):
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
