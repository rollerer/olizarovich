
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def desimal2binary(value):
    return[int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    v=[0]*8
    for i in range(7, -1, -1):
        value += 2**i
        dacc = []
        dacc = desimal2binary(value)
        GPIO.output(dac, dacc)
        sleep(0.001)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            value -= 2**i
        else:
            v[i]=1
    return value

try:
    while True:
        a = int(adc()/256*8)
        b = [0]*(8-a)+[1]*a
        print(a, b)
        GPIO.output(leds, b)

finally:
    GPIO.cleanup()
with open('data.txt', 'w') as d:
    d.write("\n".join([str(i) for i in a]))
