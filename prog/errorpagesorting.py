#!/usr/bin/python
from operator import itemgetter
fh = open('file.txt')
error_dict = {}
for line in fh:
    x = line.rstrip().split(" ")
    #print x
    if x[0] in error_dict:
        if x[1] == 'notfound':
            error_dict[x[0]] += 1
    else:
        if x[1] == 'notfound':
            error_dict[x[0]] = 1

fh.close()
print error_dict
print "sorted dictionary",sorted(error_dict,reverse = True,key= itemgetter(1))
        

    
