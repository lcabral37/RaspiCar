#!/usr/bin/bash
ps aux | grep auto.py | awk '{split($0,a," "); print a[2]}' | xargs sudo kill -9
