#!/usr/bin/env python

import time
from wc import *
from wcVariables import *

initialize()
lastDistance = SONAR_MINIMUM_DISTANCE + 1

while True:
    distance = getDistance()
    print "distance = %s" % distance 

    if distance < SONAR_MINIMUM_DISTANCE:
        if lastDistance < SONAR_MINIMUM_DISTANCE:
            print "rotating right "
            stop()
            time.sleep(LOOK_SMART_TIME)
            hardRight()
            time.sleep(TURN_TIME)
            forward()

    lastDistance = distance
    time.sleep(SONAR_AUTO_TIME)