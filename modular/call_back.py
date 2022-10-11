import RPi.GPIO as GPIO
import time 

class CallBack:
    def __init__(self, PIN=4):
       # 4番pinを入力、プルアップに設定
        self.PIN = PIN
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.IN, GPIO.PUD_UP) 

        # 割り込みイベント設定
        # 割り込みを検知するpin番号、エッジ、バウンスタイムを設定
        GPIO.add_event_detect(self.PIN, GPIO.RISING, bouncetime=1000)
        # コールバック関数登録
        #pin ⇒ GPIO4番ピン
        #self.my_callback_two ⇒ 割り込み検知後に実行される関数名
        GPIO.add_event_callback(self.PIN, self.my_callback_one) 
        GPIO.add_event_callback(self.PIN, self.my_callback_two)

    def my_callback_one(self, channel):
        print('Callback one')

    def my_callback_two(self, channel):
        print('Callback two')

    def callback_test(self):
        while True:
            time.sleep(1)

            cb = CallBack()
            cb.callback_test() # 割り込みイベント待ち))))''))''))))))))
