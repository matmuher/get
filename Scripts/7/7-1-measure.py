
import RPi.GPIO as RPi
import time
import matplotlib.pyplot as plt


# Set GPIO pins

dac = [26, 19, 13, 6, 5, 11, 9, 10]

leds = [21, 20, 16, 12, 7, 8, 25, 24]

bit_depth = 8

comp = 4

troyka = 17

maxVoltage = 3.258

max_voltage_units = 255



# Transfer decimal value to binary (bits are packaged in list)
def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# Set lead for some value
def set_leds (value):

    RPi.output (leds, decimal2binary (value))


# Get voltage from troyka module
def adc():

    right_border = 255

    left_border = 0

    for i in range (bit_depth):
         
        middle = ( right_border - left_border ) // 2 + left_border
       
        RPi.output (dac, decimal2binary (middle))

        time.sleep(0.005)

        comp_status = RPi.input (comp) 

        if (comp_status == 0):

            right_border = middle - 1

        elif (comp_status == 1):

            left_border = middle
   
    return middle


def capacity_charge ():

    measures_list = list ()

    # Set voltage for charging capacitor
    RPi.output (troyka, RPi.HIGH)

    # Start value
    cur_vol = -1

   
    upper_voltage_limit = max_voltage_units * 0.9

    while (cur_vol < upper_voltage_limit):

        cur_vol = adc ()
        measures_list.append (cur_vol)
        print ('Charging', cur_vol, upper_voltage_limit)

    return measures_list


def capacity_discharge ():

    measures_list = list ()

    # Set voltage for charging capacitor
    RPi.output (troyka, 0)

    # Start value
    cur_vol = 255

    lower_voltage_limit = max_voltage_units * 0.05

    while (cur_vol > lower_voltage_limit):

        cur_vol = adc ()
        measures_list.append (cur_vol)
        print ('Discharging', cur_vol, lower_voltage_limit)

    return measures_list


if __name__ == '__main__':

    RPi.setmode (RPi.BCM)

    # Dac pins for writing voltage
    RPi.setup(dac, RPi.OUT)

    # Led pins for writing voltage
    RPi.setup(leds, RPi.OUT)

    # Setup troyka pin for writing voltage
    RPi.setup(troyka, RPi.OUT)

    # Setup comparator pin for reading voltage
    RPi.setup(comp, RPi.IN)

    try:

        start_time = time.time()

        measures = capacity_charge()

        measures += capacity_discharge ()

        N = len(measures)

        experiment_time = time.time() - start_time

        oscillation_rate = N / experiment_time

        with open('settings.txt', 'w+') as file:

            str_to_write = str(oscillation_rate) + '\n'

            file.write(str_to_write)

            str_to_write = str(maxVoltage / max_voltage_units) + '\n'

            file.write(str_to_write)

        with open('data.txt', 'w+') as file:

            file.write('\n'.join(str(x) for x in measures))

        print(f'Период эксперимента: {experiment_time}\n')
        print(f'Период измерения: {experiment_time / N}\n')
        print(f'Ср частота дискретизации: {oscillation_rate}\n')
        print(f'Шаг квантования: {maxVoltage / max_voltage_units}\n')

        plt.scatter(list (range (len (measures))), measures)

        plt.savefig('my_graph.png')


    except Exception as ex:

        print (ex)

    finally:

        print ('[PROGRAMM COMPLETION]')

        RPi.output(dac, 1)

        time.sleep(1.5)

        RPi.output(dac, 0)

        RPi.cleanup()


