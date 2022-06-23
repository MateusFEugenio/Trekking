import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

teste1 = 16
teste2 = 12

sensor3 = 11

GPIO.setup(sensor3,GPIO.IN)

GPIO.setup(teste1,GPIO.OUT)
GPIO.setup(teste2,GPIO.OUT)

try:
    while True:
        if GPIO.input(sensor3) == False:
            print("algo detectado")
            GPIO.output(teste1,True)
            GPIO.output(teste2,False)
           
            time.sleep(1)
        else:
            GPIO.output(teste1,False)
            GPIO.output(teste2,False)
            print("sensor lendo")
            time.sleep(1)
        
except KeyboardInterrupt:
    print("deligado do projeto")
    GPIO.cleanup()