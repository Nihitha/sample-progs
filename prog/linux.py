#!/usr/bin/python

import subprocess

p = subprocess.check_output(["cat", "linkedlist.py"])#, stderr=subprocess.STDOUT)
print p.split()[1].split()[0]
 
