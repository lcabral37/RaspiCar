import RPi.GPIO as GPIO
import time

def initialize():
   GPIO.setmode(GPIO.BOARD)

   GPIO.setup(11, GPIO.OUT)
   GPIO.setup(12, GPIO.OUT)
   GPIO.setup(15, GPIO.OUT)
   GPIO.setup(16, GPIO.OUT)

def isForward():
   GPIO.setup(11, GPIO.IN)
   isforward = GPIO.input(11)
   GPIO.setup(11, GPIO.OUT)
   return isForward

def left():
   if isForward():
      GPIO.output(11, 0)
      GPIO.output(12, 0)
      GPIO.output(15, 1)
      GPIO.output(16, 0)
      time.sleep(2)
      GPIO.output(11, 1)
      GPIO.output(12, 0)
      GPIO.output(15, 1)
      GPIO.output(16, 0)
   else:
      GPIO.output(11, 0)
      GPIO.output(12, 1)
      GPIO.output(15, 0)
      GPIO.output(16, 0)
      time.sleep(2)
      GPIO.output(11, 0)
      GPIO.output(12, 1)
      GPIO.output(15, 0)
      GPIO.output(16, 1)

