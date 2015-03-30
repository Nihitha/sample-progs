#!/usr/bin/python
def fibn(n):
    a, b = 0, 1
    counter = 0
    while counter < n:
        print  a
        a, b = b, a+b
        counter += 1
n = raw_input ("enter the nth value of fib,")
fibn(int(n))












