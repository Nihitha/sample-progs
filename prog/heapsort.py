#!/usr/bin/python

def heapify(array,i,last):
    if (2*i+1) <= last:
        maximum = (2*i + 1)
        if (2*i + 2) <= last and array[2*i + 2] > array[maximum]:
            maximum = (2*i + 2)
            
        if array[i] > array[maximum]:
            return 
        else:
            x = array[i]
            array[i] = array[maximum]
            array[maximum] = x
            heapify(array,maximum,last)
   
    else:
        return
                
def build_heap(array):
    i = (len(array) - 1)/2
    while i >= 0:
        heapify(array,i,(len(array)-1))
        i -= 1
    print ("build heap is ",array)


def sort(array):
    build_heap(array)
    n = (len(array) - 1)
    while n > 0 :
        x = array[n]
        array[n] = array[0]
        array[0] = x
        heapify(array,0,n-1)
        n -= 1
    return



array = [2, 5, 3, 7, 1, 8,-10]
sort(array)
print array
