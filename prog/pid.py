#!/usr/bin/python
import re
fh = open('ps.txt')
pid_dict = {}
for line in fh:
    nl = line.rstrip().split(" ")
    #print nl[3],nl[4]
    pid,ppid  = nl[3],nl[4]
    if ppid in pid_dict:
        pid_dict[ppid].append(pid)

    else:
        pid_dict[ppid] = [pid]

print pid_dict
