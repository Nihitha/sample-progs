#!/usr/bin/python

def fibonachi(n):
    #print ("The value of fib is" , n )
    if n == 0:
        return n 
    elif n ==1:
        return n 
    else:
      return fibonachi(n-1) + fibonachi(n-2)


x = fibonachi(7)
print x 

