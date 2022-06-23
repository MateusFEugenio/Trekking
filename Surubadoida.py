import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

teste1 = 20
teste2 = 21


sensor1 = 5
sensor2 = 0
sensor3 = 11


GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(sensor3,GPIO.IN)

GPIO.setup(teste1,GPIO.OUT)
GPIO.setup(teste2,GPIO.OUT)

try:
    n = 0
    while True:
        GPIO.output(teste1, True)
        GPIO.output(teste2, False)
        print("to vivo: ", n)
        n = n + 1
             
        
except KeyboardInterrupt:
    print("deligado do projeto")
    GPIO.cleanup()

