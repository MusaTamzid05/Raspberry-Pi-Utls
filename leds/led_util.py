from RPi import GPIO
from time import sleep
from time import time

from gpio_led import Led
from safe_gpio import safe_main



def sleep_for(led , delay_time_seconds , show_time_passed = False):

    led.turn_on()
    wait( delay_time_seconds = delay_time_seconds , show_time_passed = True)
    led.turn_off()


def wait(delay_time_seconds , show_time_passed):

    if show_time_passed == False:
        sleep(delay_time_seconds)
        return

    start_time = time()
    time_passed_seconds = 0
    last_time = start_time


    while  time_passed_seconds < delay_time_seconds:

        current_time = time()
        time_passed_seconds =  current_time - start_time



        if int(current_time - last_time) == 1:
            print(" {} seconds passed of  {} seconds".format(int(time_passed_seconds) , delay_time_seconds))
            last_time = current_time









def main():


    led = Led(gpio_number = 18)
    sleep_for( led = led , delay_time_seconds = 5 , show_time_passed = True)



if __name__ == "__main__":
    safe_main(main)
