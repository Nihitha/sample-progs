#!/usr/bin/python


def merge_sort(A,left,right):
    print ("left is %d , right is %d, A is %s " %(left,right,A[left:right]))
    if len(A) > 1:
        center = (left + right) /2
        print ("left is %d , center is %d, A is %s " %(left,center,A[left:center]))
        array_left = merge_sort(A[left:center],left,center)
        print ("center is %d , right is %d, A is %s " %(center,right,A[center:right]))
        array_right =  merge_sort(A[center:right],0,len(A[center:right]))
        print ("left array is %s and right array is %s"%(array_left,array_right)) 
        sorted_array = merge(array_left,array_right)
        return sorted_array
    else:
        return A

def merge(array_left,array_right):
    new_array = []
    i, j = 0, 0
    while i < len(array_left) and j < len(array_right):
        
        if array_left[i] <= array_right[j]:
            new_array.append(array_left[i])
            i += 1 
        else:
            new_array.append(array_right[j])
            j += 1
        if i == len(array_left):
            for j_new in xrange(j,len(array_right)):
                new_array.append(array_right[j_new])
                j += 1
            
        if j == len(array_right):
            for i_new in xrange(i,len(array_left)):
                new_array.append(array_left[i_new])
                i += 1 
    print ("new array is ",new_array)
    return new_array 


A = [3, 2, 5, 1, 7, 4, -10]
res = merge_sort(A,0,len(A))
print res         

