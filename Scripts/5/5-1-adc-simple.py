
import RPi.GPIO as RPi

import time
  

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():

    for value in range(256):


        RPi.output (dac, decimal2binary (value))
        
        time.sleep(0.005)

        if (RPi.input (comp) == 0):

            return value
    
    return -1


dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

maxVoltage = 3.258


RPi.setmode (RPi.BCM)

RPi.setup(dac, RPi.OUT)

RPi.setup(troyka, RPi.OUT, initial = RPi.HIGH)

RPi.setup(comp, RPi.IN)

try:

    while True:

        value = adc ()

        print (f'Current voltage is {value / 255.0 * maxVoltage} [{value}]') 


except Exception as ex:

    print (ex)

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()

