"""
This is an implementation of insertion sort that presents the running time
for best case and worst case.
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
import time

def insertSort(length,array):

	for i in range(1,length): 
		cur = array[i]
		prev = i-1 
		while prev >=0 and cur < array[prev] :
			array[prev+1] = array[prev]
			prev -= 1
		array[prev+1] = cur
	print("--- %s seconds ---" % (time.time() - start_time))	

#main
nums = input("Number of values: ")
BCArray = []
WCArray = []
for x in range(0, nums):
    BCArray.append(x)

for x in range(nums, 0, -1):
    WCArray.append(x)

start_time = time.time()
insertSort(nums,BCArray)
print("Best Case time = --- %s seconds ---" % (time.time() - start_time))	

start_time = time.time()
insertSort(nums,WCArray)
print("Worst Case time = --- %s seconds ---" % (time.time() - start_time))	

