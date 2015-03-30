#!/usr/bin/python
import subprocess

#subprocess.check_call(["ls" , "-l"])
x = subprocess.Popen(["ls","-l"],stdout = subprocess.PIPE)
print x.stdout.read()
