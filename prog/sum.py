#!/usr/bin/python
x, y = 5, 2
def sum(x,y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry <<1
    return x


s = sum(x,y)
print s
