#!/usr/bin/python

import re
fh = open("phonebook.txt")
for line in fh:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)",line)
    print res.group(3) + " " + res.group(2)+ res.group(1)
fh.close()

