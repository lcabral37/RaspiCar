#!/usr/bin/env python
import cgi
import commands
import cgitb
# from subprocess import call
# call([shell])


cgitb.enable()
form = cgi.FieldStorage()
cmd  = form.getvalue("cmd", "(no cmd)")

shell = "sudo /var/www/WC/" + cmd + ".py"
status, output = commands.getstatusoutput(shell)


print "Content-Type: text/html"
print
print output
