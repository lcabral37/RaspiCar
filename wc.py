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

   GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
   GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

   GPIO.output(GPIO_TRIGGER, False)

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
      time.sleep(TURN_TIME)
      forward()
   else:
      lightRightBackward()
      time.sleep(TURN_TIME)
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

def getDistance():
   # Allow module to settle
   #time.sleep(0.5)

   # Send 10us pulse to trigger
   GPIO.output(GPIO_TRIGGER, True)
   time.sleep(0.00001)
   GPIO.output(GPIO_TRIGGER, False)
   start = time.time()
   while GPIO.input(GPIO_ECHO)==0:
     start = time.time()

   while GPIO.input(GPIO_ECHO)==1:
     stop = time.time()

   # Calculate pulse length
   elapsed = stop-start

   # Distance pulse travelled in that time is time
   # multiplied by the speed of sound (cm/s)
   distance = elapsed * 34000

   # That was the distance there and back so halve the value
   distance = distance / 2
   return distance
