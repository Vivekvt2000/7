#!/usr/bin/python3
print("content-type: text/html")     # this line is used by the  browser as Head of Website
print()                              # used to seprate Head of website to its Body

import cgi                           # CGI is Common Gateway Interface between client and server
import subprocess

y = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput(cmd)
print(output)
