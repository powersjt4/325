"""
This is an implementation of insertion sort that presents the running time
for average case.
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
import time
import random 

nums = input("Number of random values: ")
array = []
for x in range(nums):
    array.append(random.randint(0,10000))
length = nums
start_time = time.time()
for i in range(1,length): 
    cur = array[i]
    prev = i-1 
    while prev >=0 and cur < array[prev] :
        array[prev+1] = array[prev]
        prev -= 1
    array[prev+1] = cur
print("--- %s seconds ---" % (time.time() - start_time))

