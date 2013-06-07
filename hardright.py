#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

isforward = GPIO.input(11)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

if isforward:
   GPIO.output(11, 0) 
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 0)
   GPIO.output(11, 1)
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 1)
   time.sleep(2)
   GPIO.output(11, 0) 
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 0)
else:
   GPIO.output(11, 0)
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 0)

   GPIO.output(11, 0)
   GPIO.output(12, 1)
   GPIO.output(15, 1)
   GPIO.output(16, 0)
   time.sleep(2)
   GPIO.output(11, 0) 
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 0)
