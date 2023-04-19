import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(troyka, GPIO.OUT)

def ToBin(a, n):
    return [int(elem) for elem in bin(a)[2:].zfill(n)]

print(ToBin(8, 8))

def adc():
    for i in range(256):
        
        sig = ToBin(i,8)
        GPIO.output(dac, sig)
        sleep(0.001)
        if GPIO.input(comp) ==0:  

            break 
    return(i)



try:
    while True:
        value = adc()

        if value!=0:
            V = value*3.3/256
            V /= 0.4
            print(V)
            V = int(V)
            print(value, V, [0]*(8-V) + [1]*V)
            GPIO.output(leds, [0]*(8-V) + [1]*V)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()  