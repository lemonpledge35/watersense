import RPi.GPIO as GPIO
import time

def read_pin(pin_number):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.IN)
    try:
        state = GPIO.input(pin_number)
        if state == GPIO.HIGH:
            return 1
        else:
            return 0
    except:
        return 2
    finally:
        GPIO.cleanup()




if __name__ == "__main__"

INPUT_PIN = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.IN)
    try:
        while True:

            state = GPIO.input(INPUT_PIN)
            if state == GPIO.HIGH:
                print("Pin is high")
            else:
                print("Pin is low")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exciting")
    finally:
        GPIO.cleanup()