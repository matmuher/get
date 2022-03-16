def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

import RPi.GPIO as RPi
import time

sleep_time = 1.5

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RPi.setmode(RPi.BCM)
RPi.setup(dac, RPi.OUT)

max_volt = 3.258
saw_period = 2
ticks_num = 256

try:
        
    saw_tick = saw_period / ticks_num

    for i in range (2):
         
        i = 0
        t = 0

        while (t < saw_period):

            t_start = time.time()

            dac_out = decimal2binary(i) 

            RPi.output(dac, dac_out)

            i += 1
            t += saw_tick

            t_end = time.time()

            time.sleep(saw_tick - (t_end - t_start));


except Exception as ex:

    print(ex)

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()