from RPi import GPIO
from time import sleep
from safe_gpio import safe_main




class Led:

    def __init__(self , gpio_number):


        self.gpio_number = gpio_number
        GPIO.setup(self.gpio_number , GPIO.OUT)
        self._on = False


    def is_on(self):
        return self._on


    def turn_on(self, delay = None):

        GPIO.output(self.gpio_number , True)
        self._on = True

    def turn_off(self):

        if self._on == False:
            print("{} led is not on.".format(self.gpio_number))
            return

        GPIO.output(self.gpio_number , False)


    def beep_for(self , times , delay_seconds = 1.0):

        for _ in range(times):

            self.turn_on()
            sleep(delay_seconds)
            self.turn_off()
            sleep(delay_seconds)


def main():

    led = Led(gpio_number = 18)
    led.beep_for(times = 5 , delay_seconds = 0.5)



if __name__ == "__main__":
    safe_main(main)





