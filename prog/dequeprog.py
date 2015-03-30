#!/usr/bin/python

from collections import deque

d = deque('ghi')
for elem in d:
    print elem.upper()

d.append('q')
d.appendleft('b')
print list(d)
d.pop()
d.popleft()
print list(d)
