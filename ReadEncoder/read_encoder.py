import sys
import RPi.GPIO as GPIO
import time

class ReadEncoder:
    def __init__(self, RoAPin=11, RoBPin=12):
        self.RoAPin = RoAPin
        self.RoBPin = RoBPin
        self.globalCounter = 0
        self.is_inspect_complete = False
        self.Last_RoB_Status = 0
        self.Current_RoB_Status = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RoAPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.RoBPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def rotaryDeal(self):
        start = time.time()
        self.Last_RoB_Status = GPIO.input(self.RoBPin)
        while (not GPIO.input(self.RoAPin)):
            self.Current_RoB_Status = GPIO.input(self.RoBPin)
            self.is_inspect_complete = True

        if self.is_inspect_complete:
            self.is_inspect_complete = False
            self.globalCounter +=  self.Current_RoB_Status - self.Last_RoB_Status
        return time.time() - start

    def loop(self):
        while True:
            preGlobalCounter = self.globalCounter
            deal_time = self.rotaryDeal()
            if (preGlobalCounter != self.globalCounter):
                print(f"globalCounter {self.globalCounter}")
                print(f"{(self.globalCounter - preGlobalCounter)/(600 * deal_time)} Hz")
            if (self.globalCounter >= 600):
                self.globalCounter -= 600

    def destroy(self):
        GPIO.cleanup()

if __name__ == '__main__':
    argv = sys.argv
    Encoder_Reader = ReadEncoder() if len(argv) <= 2 else ReadEncoder(int(argv[1]), int(argv[2]))

    try:
        Encoder_Reader.loop()
    except KeyboardInterrupt:
        Encoder_Reader.destroy()
        print("Finished by keyboard interrupt")
