import RPi.GPIO as GPIO
import time
#GPIO.setwarnings(False)

from wcVariables import *

def initialize():
   GPIO.setmode(GPIO.BOARD)

   GPIO.setup(GPIO_LEFT_FORWARD, GPIO.OUT)
   GPIO.setup(GPIO_LEFT_BACK, GPIO.OUT)
   GPIO.setup(GPIO_RIGHT_FORWARD, GPIO.OUT)
   GPIO.setup(GPIO_RIGHT_BACK, GPIO.OUT)

def isForward():
   GPIO.setup(GPIO_LEFT_FORWARD, GPIO.IN)
   isforward = GPIO.input(GPIO_LEFT_FORWARD)
   GPIO.setup(GPIO_LEFT_FORWARD, GPIO.OUT)

   GPIO.setup(GPIO_LEFT_BACK, GPIO.IN)
   isbackward = GPIO.input(GPIO_LEFT_BACK)
   GPIO.setup(GPIO_LEFT_BACK, GPIO.OUT)
   return not isbackward

def left():
   if isForward():
      GPIO.output(GPIO_LEFT_FORWARD, 0)
      GPIO.output(GPIO_LEFT_BACK, 0)
      GPIO.output(GPIO_RIGHT_FORWARD, 1)
      GPIO.output(GPIO_RIGHT_BACK, 0)
      time.sleep(2)
      GPIO.output(GPIO_LEFT_FORWARD, 1)
      GPIO.output(GPIO_LEFT_BACK, 0)
      GPIO.output(GPIO_RIGHT_FORWARD, 1)
      GPIO.output(GPIO_RIGHT_BACK, 0)
   else:
      GPIO.output(GPIO_LEFT_FORWARD, 0)
      GPIO.output(GPIO_LEFT_BACK, 1)
      GPIO.output(GPIO_RIGHT_FORWARD, 0)
      GPIO.output(GPIO_RIGHT_BACK, 0)
      time.sleep(2)
      GPIO.output(GPIO_LEFT_FORWARD, 0)
      GPIO.output(GPIO_LEFT_BACK, 1)
      GPIO.output(GPIO_RIGHT_FORWARD, 0)
      GPIO.output(GPIO_RIGHT_BACK, 1)

def right():
   if isForward():
      lightRightForward()
      time.sleep(2)
      forward()
   else:
      lightRightBackward()
      time.sleep(2)
      backward()

def lightRightForward():
      GPIO.output(11, 1) 
      GPIO.output(12, 0)
      GPIO.output(15, 0)
      GPIO.output(16, 0)

def lightRightBackward():
      GPIO.output(11, 0)
      GPIO.output(12, 0)
      GPIO.output(15, 0)
      GPIO.output(16, 1)

def forward():
      GPIO.output(11, 1)
      GPIO.output(12, 0)
      GPIO.output(15, 1)
      GPIO.output(16, 0)

def backward():
      GPIO.output(11, 0)
      GPIO.output(12, 1)
      GPIO.output(15, 0)
      GPIO.output(16, 1)

def stop():
      GPIO.output(11, 0)
      GPIO.output(12, 0)
      GPIO.output(15, 0)
      GPIO.output(16, 0)

def hardLeft():
   GPIO.output(11, 0)
   GPIO.output(12, 1)
   GPIO.output(15, 1)
   GPIO.output(16, 0)

def hardRight():
   GPIO.output(11, 1)
   GPIO.output(12, 0)
   GPIO.output(15, 0)
   GPIO.output(16, 1)
