#!/usr/bin/python
lists = [2, 3, 6, 7,8]
number = int(raw_input("Enter the number to search,"))
for i, j in enumerate(lists):
    if j == number:
        print i
        
#for list comprehensions 
x = [i for i,j in enumerate(lists) if j==number] 
print x  


print lists.index(number)      
