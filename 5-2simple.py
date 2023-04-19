import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(troyka, GPIO.OUT)

def ToBin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

print(ToBin(8, 8))

def adc():
    n = 0
    
    for i in range(7,-1, -1):
        n += 2**i
        sig = ToBin(i,8)
        GPIO.output(dac, sig)
        sleep(0.005)
        if GPIO.input(comp) ==0:  
            n -= 2**i
            
        




    
    return n



try:
    while True:
        value = adc()

        if value!=0:
            V = value*3.3/256
            print(value, V)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()  