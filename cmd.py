#!/usr/bin/env python

import subprocess as s
import cgi
import commands
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
cmd  = form.getvalue("cmd", "(no cmd)")

print "Content-Type: text/html"
print

print "starting %s" % cmd
s.call("sudo /var/www/WC/" + cmd + ".py &",shell=True)

