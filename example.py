import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=17)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("日時:" + str(datetime.datetime.now()))
	        print("温度: %-3.1f C" % result.temperature)
	        print("湿度: %-3.1f %%" % result.humidity)
			with open('パス', 'a') as f:
    			writer = csv.writer(f)
    			writer.writerow(["日時:" + str(datetime.datetime.now()), "温度: %-3.1f C" % result.temperature, "湿度: %-3.1f %%" % result.humidity])
	    time.sleep(10)
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()