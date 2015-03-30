#!/usr/bin/python

a = {}
a[1] = "abc"
a[2] = "cdf"
for key,value in a.iteritems():
    print key,value 

for k in a.iterkeys():
    print k 
    
a = {1:"abc",2:"cdf"}
s  = set(a)
print s
