from RPi import GPIO
import logging


GPIO_BCM_MODE = 11


def safe_main(func):
    '''
    This ensure the GPIO are safely turn on and off.What ever program you are running, it is advisable to  call that function as parameter of this.
    '''

    GPIO.setmode(GPIO.BCM)
    print("Pin set to BCM.")

    try:
        func()
    except Exception as e:

        '''
        Very very bad practice i know,but because at the current moment i am not sure how many exception i need to handle,i am  catching Exception.
        I am so sorry :(
        '''
        logging.exception(e)

    finally:
        print("Cleaning up.")
        GPIO.cleanup()



def main():
    print("Raspberri pi running safely.")



if __name__ == "__main__":
    safe_main(main)
