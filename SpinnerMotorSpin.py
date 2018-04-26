from RPi import GPIO
import time

class Spinner():
    def SpinCounterClockWise(self, pin):
        i = 0
        while(i < 40):
            time.sleep(.0175)
            GPIO.output(pin, 1)
            time.sleep(.0025)
            GPIO.output(pin, 0)
            i += 1

    def SpinClockWise(self, pin):
        i = 0
        while (i < 40):
            time.sleep(.0185)
            GPIO.output(pin, 1)
            time.sleep(.0005)
            GPIO.output(pin, 0)
            i += 1
