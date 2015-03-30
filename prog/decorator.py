#!/usr/bin/python

def addition(x,y):
    return x+y




def outer(f):
    def add(x,y):
        ret = f(x,y)
        return ret + 1
    return add
    

addition = outer(addition)
print addition(3,4)  

