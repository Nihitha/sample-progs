#!/usr/bin/python
import re

fh = open('employee.txt','r').readlines()
#print fh
fh_str = str(fh)       
#print (type(fh_str))
#print fh_str
#x = re.split("\*{3}",fh_str)

result = re.findall(r'(\*+\\n\',)(.*)(\'\*+\\n\',)',fh_str ,re.MULTILINE)
print result
"""
if result:
    print result.group(2)
res =re.search(r'Userid:(.*)',line)
    if res:
        print res.group(1)
        res1 = re.search(r'name:(.*)',line)
        if res1:
            print res1.group(1)
            print res.group(1) +":" + res1.group(1)
            org[res.group(1)] = {name:res1.group(1)}

for key,value in org.iteritems():
    print key,value
"""
