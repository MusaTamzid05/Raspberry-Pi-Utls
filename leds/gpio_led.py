from RPi import GPIO
from time import sleep
from safe_gpio import safe_main




class Led:

    def __init__(self , gpio_number):


        self.gpio_number = gpio_number
        GPIO.setup(self.gpio_number , GPIO.OUT)
        self._on = False

        self._init_light_freq(hertz = 100)

    def _init_light_freq(self , hertz):

        self.pwd_led = GPIO.PWM(self.gpio_number , hertz)
        self.pwd_led.start(100) # starting the duty circle with 100 %


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


    def set_light_brightness(self , brightness_value):

        if brightness_value < 0 or brightness_value > 100:
            raise RuntimeError("brightness value is a percentage and it should be between 0 and 100.")

        self.pwd_led.ChangeDutyCycle(brightness_value)


def test_beeping():

    led = Led(gpio_number = 18)
    led.beep_for(times = 5 , delay_seconds = 0.5)

def test_brightness():

    led = Led(gpio_number = 18)
    led.turn_on()

    while True:

        brightness_value = input("Enter the brightness value (0-100) or enter 'q' to quit:")

        if brightness_value == "q":
            print("Time to break")
            break


        led.set_light_brightness(int(brightness_value))




if __name__ == "__main__":
    safe_main(test_brightness)





