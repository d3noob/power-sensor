#!/usr/bin/python
#encoding:utf-8

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)
ads.gain = 1

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

#print("{:>5}\t{:>5}".format('raw', 'v'))

while True:

  readValue = 0         
  maxValue = 0      
  
  for i in range(0,300):
    readValue = chan.value
       
    if (readValue > maxValue):         
      maxValue = readValue

  # write the current integer value to a file
  f = open("current.txt", "w")
  f.write(str(maxValue-6680))
  f.close()

#  print("{:>5}\t{:>5.5f}".format(maxValue-6680, chan.voltage))
  time.sleep(0.5)
