import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(14, RPi.GPIO.OUT)
RPi.GPIO.setup(15, RPi.GPIO.IN)

print("1")

while True:
    if RPi.GPIO.input(15):
        RPi.GPIO.output(14, 1)
        print("1")
    else:
        RPi.GPIO.output(14, 0)
        print("0")
    