#!/usr/bin/env python

import time
from wc import *

initialize()
forward()

while True:
    distance = getDistance()
    if distance < SONAR_MINIMUM_DISTANCE:
        stop()
        time.sleep(1)
        hardRight()
        time.sleep(2)
        forward()

    #print "distance = %s" % distance 
    time.sleep(0.2)