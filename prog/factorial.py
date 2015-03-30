#!/usr/bin/python
def argument_test_natural_number(f):
    def helper(x):
        print f,x,f(x) 
        if type(x) == int and x > 0:
             return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def fact(n):
    #print("the string for factorial is",n)
    if n== 1:
        return n
    else:
        res = n * fact(n-1)
        return res


x = fact(8)
print x


