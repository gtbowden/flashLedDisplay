import os
import glob
import time
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# you must get your address (28-0000....) of each DS18B20 one wire sensor elsewhere
# see https://www.waveshare.com/wiki/Raspberry_Pi_Tutorial_Series:_1-Wire_DS18B20_Sensor
outside_file = "/sys/bus/w1/devices/28-00000d92d684/temperature"
inside_file = "/sys/bus/w1/devices/28-00000d92989c/temperature"

GPIO.setmode(GPIO.BCM)
LED = 21 # The GPIO pin wired to the LED.
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

def read_temp_raw(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
#   linestring=lines[0]
    temperature=int(lines[0])
    return temperature

# main forever loop
while True:
    insidetemp=read_temp_raw(inside_file)
    outsidetemp=read_temp_raw(outside_file)
    # inside and outsidetemp are raw: e.g. 24590 meaning 24.590 degrees C

    #flash LED long for temperature tens's digit (broken for temperatures < zero)
    i=10000
    while i< outsidetemp: #flash once for each tens count, e.g. twice for 24790
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(.5)
        #print ("LED off",i)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(.5)
        print("firstloop",i)
        i=i+10000

    #flash LED short for temperature one's digit, e.g. 5 times for 24790
    i=outsidetemp % 10000
    while i>0:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(.2)
        #print ("LED off")
        GPIO.output(LED,GPIO.LOW)
        time.sleep(.2)
        print("Secondloop",i)
        i=i-1000

    #This is for testing...See output on terminal
    result = time.localtime()

#   print("result:", result)
    print("\n",result.tm_year,result.tm_mon,result.tm_mday, ",", result.tm_hour, ":", result.tm_min,\
        "  inside=", insidetemp, "outside=", outsidetemp)
    time.sleep(3)
