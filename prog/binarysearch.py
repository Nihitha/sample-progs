#!/usr/bin/python
def bsearch(array,left,right,x):
    if left < right: 
        center = (left + right)/ 2
        #print ("center is ",center)
        if array[center] > x:
            return bsearch(array,left,center-1,x)
        elif array[center] == x:
            return center
        else:
            return bsearch(array,center+1,right,x)
    else:
         if array[right] == x:
             return right
         elif array[left] == x:
             return left
         else:
             return



array = [0, 5, 15, 20, 25, 27]
x = int(raw_input("Enter the number you want to search,"))
pos = bsearch(array,0,(len(array)-1),x)
print ("position of element in the list is ",pos)
