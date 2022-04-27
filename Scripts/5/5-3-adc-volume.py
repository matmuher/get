
import RPi.GPIO as RPi

import time
  

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc1():

    

    right_border = 255

    left_border = 0

    for i in range (bit_depth):
         
        middle = ( right_border - left_border ) // 2 + left_border
        # print (middle)
        RPi.output (dac, decimal2binary (middle))

        time.sleep(0.005)

        comp_status = RPi.input (comp) 

        # print (f'Comp status is {comp_status}')

        if (comp_status == 0):

            right_border = middle - 1

        elif (comp_status == 1):

            left_border = middle
   
    return middle


def adc2():

    for value in range(256):


        RPi.output (dac, decimal2binary (value))
        
        time.sleep(0.005)

        if (RPi.input (comp) == 0):

            return value
    
    return -1



dac = [26, 19, 13, 6, 5, 11, 9, 10]

leds = [21, 20, 16, 12, 7, 8, 25, 24]

bit_depth = 8

comp = 4

troyka = 17

maxVoltage = 3.216


RPi.setmode (RPi.BCM)

RPi.setup(dac, RPi.OUT)

RPi.setup(troyka, RPi.OUT, initial = RPi.HIGH)

RPi.setup(leds, RPi.OUT, initial = RPi.LOW)

RPi.setup(comp, RPi.IN)


rejime = 1

period = 256 // 8



try:

    while True:
        
        

        if (rejime):
            
            value = adc1 () 

        else:

            value = adc2 ()

    

        part = value // period

        val_bin = [0] * 8

        print (value, value / 250.0 * maxVoltage)

        if (value != 0):

            val_bin[part] = 1

            flag = 0

            for i in range(7, -1, -1):
                
                if (val_bin[i]):

                    flag = 1

                if (flag):
                    val_bin[i] = 1

        # print (val_bin)

        RPi.output (leds, val_bin)


except Exception as ex:

    print (ex)

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()

