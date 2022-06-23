import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor1 = 5
sensor2 = 0
sensor3 = 11

Led = 23
GiroflexA = 26
GiroflexB = 19


'''
DireçãoA HIGH
DireçãoB LOW
         Vira para a direita
         
DireçãoA LOW
DireçãoB HIGH
         Vira para a esquerda
'''
DireçãoA = 16
DireçãoB = 12


'''
MotorTA HIGH
MotorTB LOW
         Vira para a frente
         
MotorTA LOW
MotorTB HIGH
         Vira para a tras
'''
MotorTA = 13
MotorTB = 6


'''
MotorFA HIGH
MotorFB LOW
         Vira para a frente
         
MotorFA LOW
MotorFB HIGH
         Vira para a tras
'''
MotorFA = 20
MotorFB = 21

GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(sensor3,GPIO.IN)

GPIO.setup(Led,GPIO.OUT)
GPIO.setup(GiroflexA,GPIO.OUT)
GPIO.setup(GiroflexB,GPIO.OUT)

GPIO.setup(DireçãoA,GPIO.OUT)
GPIO.setup(DireçãoB,GPIO.OUT)
GPIO.setup(MotorTA,GPIO.OUT)
GPIO.setup(MotorTB,GPIO.OUT)
GPIO.setup(MotorFA,GPIO.OUT)
GPIO.setup(MotorFB,GPIO.OUT)

GPIO.output(DireçãoA, False)
GPIO.output(DireçãoB, False)
GPIO.output(MotorTA, False)
GPIO.output(MotorTB, False)
GPIO.output(MotorFA, False)
GPIO.output(MotorFB, False)


try:
    while True:        
        if GPIO.input(sensor1) == False:
            print("S1")
            
            GPIO.output(Led,True)
            GPIO.output(GiroflexB,True)
            GPIO.output(GiroflexA,False)
            
            GPIO.output(DireçãoA, True)
            GPIO.output(DireçãoB, False)
            
            GPIO.output(MotorTA, True)
            GPIO.output(MotorTB, False)
            GPIO.output(MotorFA, False)
            GPIO.output(MotorFB, False)
            
        elif GPIO.input(sensor2) == False:
            print("S2")
            
            GPIO.output(Led,True)
            GPIO.output(GiroflexB,True)
            GPIO.output(GiroflexA,False)
            
            GPIO.output(DireçãoA, False)
            GPIO.output(DireçãoB, True)
            
            GPIO.output(MotorTA, True)
            GPIO.output(MotorTB, False)
            GPIO.output(MotorFA, False)
            GPIO.output(MotorFB, False)
            
        elif GPIO.input(sensor3) == False:
            print("S3 - Pare")
            
            GPIO.output(GiroflexB,True)
            GPIO.output(GiroflexA,False)
            
            GPIO.output(DireçãoA, False)
            GPIO.output(DireçãoB, False)
            GPIO.output(MotorTA, False)
            GPIO.output(MotorTB, False)
            GPIO.output(MotorFA, False)
            GPIO.output(MotorFB, False)
            
            time.sleep(0.1)
        else:
            print("andar para frente")
            
            GPIO.output(DireçãoA, False)
            GPIO.output(DireçãoB, False)
            
            GPIO.output(MotorTA, True)
            GPIO.output(MotorTB, False)
            GPIO.output(MotorFA, True)
            GPIO.output(MotorFB, False)
            
            time.sleep(0.1)
        
        
except KeyboardInterrupt:
    print("deligado do projeto")
    GPIO.cleanup()