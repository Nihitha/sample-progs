#!/usr/bin/python

import re

fh = open("tags.txt")
for line in fh:
    res = re.search(r"<([a-z]+)>(.*)</\1>",line)
    print res.group(1) + ":" + res.group(2)
fh.close() 
