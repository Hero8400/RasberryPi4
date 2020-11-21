import RPi.GPIO as GPIO #GPIOモジュールをインポート
import time

LedGpio = 18 #GPIO指定用の変数を設定
WaitTime = 0.3 #待機時間を指定

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedGpio, GPIO.OUT)

for i in range(20):
    GPIO.output(LedGpio, True)
    time.sleep(WaitTime)
    GPIO.output(LedGpio, False)
    time.sleep(WaitTime)

GPIO.cleanup()
