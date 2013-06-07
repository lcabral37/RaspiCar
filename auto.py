#!/usr/bin/env python

import time
from wc import *

initialize()

while True:
    distance = getDistance()
    if distance < SONAR_MINIMUM_DISTANCE:
        stop()
        time.sleep(LOOK_SMART_TIME)
        hardRight()
        time.sleep(TURN_TIME)
        forward()

    #print "distance = %s" % distance 
    time.sleep(SONAR_AUTO_TIME)