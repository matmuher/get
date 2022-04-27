def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

import RPi.GPIO as RPi
import time

sleep_time = 1.5

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RPi.setmode(RPi.BCM)
RPi.setup(dac, RPi.OUT)

RPi.setup(23, RPi.OUT)
RPi.setup (2, RPi.IN)

max_volt = 3.258
saw_period = 10
ticks_num = 256

try:
    p = RPi.PWM(23, 1000)
    p.start(50)

    while True:

        duty_cycle = int(input('Enter duty cycle please!'))

        p.start(duty_cycle)


        print('{:.3}\n'.format(duty_cycle / 100.0 * max_volt))

    p.stop()

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()