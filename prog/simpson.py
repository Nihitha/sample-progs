#/usr/bin/python

import re

fh = open("abc.txt")
for line in fh:
    if re.search(r"J[a-z].Neu",line):
        print line.rstrip()
fh.close()

