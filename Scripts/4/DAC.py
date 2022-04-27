def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

import RPi.GPIO as RPi
import time

sleep_time = 1.5

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RPi.setmode(RPi.BCM)
RPi.setup(dac, RPi.OUT)

max_volt = 3.3

try:
    while True:

        print('\nPlease, enter value in range [0;255] or \"q\" to exit:')
        
        dac_out = input ()

        if (dac_out.isdigit()):
            
            dac_out = int(dac_out)

            if (0 <= dac_out <= 255):

                expected_volt = dac_out / 255.0 * max_volt
                print('\nExpected voltage is {:.2}'.format(expected_volt))

                dac_out = decimal2binary(dac_out)

                print(dac_out)

                RPi.output(dac, dac_out)

                time.sleep (sleep_time)

            else:
                print('\n[ERORR:Bad number] Please enter number from range [0;255]\n')

                continue

        else:
            if dac_out == "q":
                break

            print('\n[ERROR:Non-digit input] Please enter digit from [0;255] or \"q\" to exit\n')

            continue

except Exception as ex:

    print(ex)

finally:

    print ('[PROGRAMM COMPLETION]')

    RPi.output(dac, 1)

    time.sleep(1.5)

    RPi.output(dac, 0)

    RPi.cleanup()