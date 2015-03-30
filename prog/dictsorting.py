#!/usr/bin/python

from operator import itemgetter
d = {'apple' : 0 , 'orange' : 5, 'grape' : 2, 'pear':3}
print sorted(d.items(),key = itemgetter(1,0),reverse = True)
print "can also be sorted using lambda"
print sorted(d.items(), reverse = True,key = lambda x:x[1])
a = ['apple','grape','orange']
print sorted (a, key = d.__getitem__)
print " in correct order "
print sorted(d.items(),key = itemgetter(1,0))
if 'orange' in d:
    print d['orange']
print d.get('apple')

