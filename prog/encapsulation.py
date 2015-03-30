#!/usr/bin/python
class encap():
    def __init__(self,name,balance,ssn):
        self.name = name
        self._balance = balance
        self.__ssn = ssn
    def getbalance(self):
        return self._balance
    def getname(self):
        return self.name
e = encap("vik",10,4734873)
print e.getbalance()
print e.name
print e._balance
print e.__ssn 
