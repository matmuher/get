
import RPi.GPIO as RPi

import time
  

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():

    

    right_border = 255

    left_border = 0

    for i in range (bit_depth):
         
        middle = ( right_border - left_border ) // 2 + left_border
        print (middle)
        RPi.output (dac, decimal2binary (middle))

        time.sleep(0.005)

        comp_status = RPi.input (comp) 

        print (f'Comp status is {comp_status}')

        if (comp_status == 0):

            right_border = middle - 1

        elif (comp_status == 1):

            left_border = middle
            

            
   
    return middle


dac = [26, 19, 13, 6, 5, 11, 9, 10]

bit_depth = 8

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

        print (f'Current voltage is {value / 255.0 * maxVoltage}') 


except Exception as ex:

    print (ex)

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()

