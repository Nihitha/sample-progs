#!/usr/bin/python
import re

fh = open('employee.txt','r')
org = {}
for line in fh:
    res = re.search(r'Userid:(\d),name:(\w*),location:([a-zA-Z]*),reports:(.*)',line)
    if res:
        #print "user id is",res.group(1)
        #print "name is ",res.group(2)
        #print "location is",res.group(3)
        #print "reports are",res.group(4) 
        org[res.group(1)] = {}
        org[res.group(1)]['name']= res.group(2)
        org[res.group(1)]['location'] = res.group(3)
        reports_list = res.group(4).split(",")
        #print reports_list
        reports = []
        for r in reports_list:
            rep = re.search(r'reports:(.*)',r)
            if rep:
                reports.append(rep.group(1))
            else:
                reports.append(r)
        #reports = re.split(",* *\w*:",str(reports_list))
        #print reports 
        org[res.group(1)]['reports'] = reports
        for key, value in org.iteritems():
            print key,value

print '****************'
print org        
