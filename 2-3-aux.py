import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
aux = [22,23,27,18,15,14,3,2]

RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
RPi.GPIO.setup(aux, RPi.GPIO.IN)

while True:
    for i in range(0, 8):
        RPi.GPIO.output(leds[i], RPi.GPIO.input(aux[i]))

RPi.GPIO.output(leds, 1)
time.sleep(0.2)
RPi.GPIO.output(leds, 0)
RPi.GPIO.cleanup()