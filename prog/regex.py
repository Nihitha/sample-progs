#!/usr/bin/python
import re


fh = open("abc.txt")
for f in fh:
    if re.search(r"[J].*Neu",f):
        print f.rstrip()
fh.close()







