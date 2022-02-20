import RPi.GPIO as GPIO
from time import sleep

class My_Raspi_GPIO_Controller:
    def __init__(self,  AN1 = 12 ,AN2 = 13, DIG1 = 26, DIG2 = 24):
        self.AN1 = AN1
        self.AN2 = AN2
        self.DIG1 = DIG1
        self.DIG2 = DIG2

        GPIO.setup(self.AN1, GPIO.OUT)
        GPIO.setup(self.AN2, GPIO.OUT)
        GPIO.setup(self.DIG1, GPIO.OUT)
        GPIO.setup(self.DIG2, GPIO.OUT)

        sleep(1)
        self.p1 = GPIO.PWM(self.AN1, 100)
        self.p2 = GPIO.PWM(self.AN2, 100)


    def turn_left(self):
        GPIO.output(self.DIG1, GPIO.HIGH)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(100)
        self.p2.start(100)
        print("Left")


    def turn_right(self):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.HIGH)
        self.p1.start(100)
        self.p2.start(100)
        print("Right")


    def go_forward(self):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(100)
        self.p2.start(100)
        print("Forward")


    def go_backward(self):
        GPIO.output(self.DIG1, GPIO.HIGH)
        GPIO.output(self.DIG2, GPIO.HIGH)
        self.p1.start(100)
        self.p2.start(100)
        print("Backward")


    def stop(self):
        GPIO.output(self.DIG1, GPIO.LOW)
        GPIO.output(self.DIG2, GPIO.LOW)
        self.p1.start(0)
        self.p2.start(0)
        print("STOP")


