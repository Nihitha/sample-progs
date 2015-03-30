#!/usr/bin/python

x =raw_input("enter the nth value of fibonachi,")
x = int(x)
def fib(n):
    print n 
    a,b,i = 0,1,0
    #yield a
    while i < n:
        yield a  
        a,b,i = b,a+b,i+1
  

for i in fib(x):
    print i    


