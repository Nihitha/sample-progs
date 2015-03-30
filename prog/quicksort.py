#!/usr/bin/python

def quicksort(a,left,right):
    if left < right:
        p = right
        j,i = left,left
        
        while i < right:
            if a[i] > a[p]:
                i += 1

            else:
                if i != j:
                    swap = a[i]
                    a[i] = a[j]
                    a[j] = swap
                j += 1
                i += 1
        swap = a[p]
        a[p] = a[j]
        a[j] = swap
        return quicksort(a,left,j-1)
        return quicksort(a,j+1,right)
    else:
        return

        
a=[9,11,-1,0,10,4,6]
quicksort(a,0,(len(a)-1))
print a             

