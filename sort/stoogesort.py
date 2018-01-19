"""
This is an implementation of insertion sort that presents the running time
for average case.
Other resources: https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort
"""
import time
import random 
import math
def StoogeSort(A,l,h):
        if (A[l] > A[h]):
            A[l],A[h] = A[h],A[l]
        
        if (h-l > 1):
	    m = int(math.ceil((h-l+1)/3))
	    StoogeSort(A,l, h-m)
	    StoogeSort(A,l+m,h)
	    StoogeSort(A,l, h-m)
#main
    
nums = input("Number of random values: ")
array = []
for x in range(nums):
    array.append(random.randint(0,10000))
length = nums
#array = [2,20,22,8,6,1,0,10,9,3]
start_time = time.time()
StoogeSort(array,0, len(array)-1)
for x in array:
    print (x)
print("--- %s seconds ---" % (time.time() - start_time))

