import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)

for i in range(3):
    for i in leds:
        RPi.GPIO.output(i, 1)
        time.sleep(0.2)
        RPi.GPIO.output(i, 0)

RPi.GPIO.output(leds, 1)
time.sleep(0.2)
RPi.GPIO.output(leds, 0)
RPi.GPIO.cleanup()
