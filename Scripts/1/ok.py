import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

GPIO.setup(17, GPIO.IN)

GPIO.output(14, GPIO.input(17))