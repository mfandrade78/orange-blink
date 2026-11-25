from machine import Pin
import time

led = Pin(23, Pin.OUT)
#led.value(1)

def piscarLed():
  while True:
    led.value(1)
    time.sleep(1)

    led.value(0)
    time.sleep(1)
piscarLed()

#simulator link on Wokwi: https://wokwi.com/projects/481614290090720257
