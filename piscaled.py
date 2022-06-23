import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Led = 23
GiroflexA = 21
GiroflexB = 20


GPIO.setup(Led,GPIO.OUT)
GPIO.setup(GiroflexA,GPIO.OUT)
GPIO.setup(GiroflexB,GPIO.OUT)

try:
    while True:
        print("led aceso")
        GPIO.output(Led,True)
        GPIO.output(GiroflexB,True)
        GPIO.output(GiroflexA,False)
        time.sleep(10)
        print("led apagado")
        GPIO.output(Led,False)
        
        GPIO.output(GiroflexA,False)
        GPIO.output(GiroflexB,False)
        time.sleep(10)
        
except KeyboardInterrupt:
    print("deligado do projeto")
    GPIO.cleanup()