"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
"""
import time
import random 

nums = input("Number of random values: ")
array = []
for x in range(nums):
    array.append(random.randint(0,10000))

#input = "data.txt"
#output = "insert.out"
#inFile = open(input, "r")
#outFile = open(output, "w")
#for line in inFile:
#        array = [] 
#        for val in line.split():
#            array.append(int(val))
#	length = int(array[0]) 
#        array.pop(0)
#        print len(array)
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
#print(array)
#for item in array:
#    outFile.write("%d "% item)
#outFile.write("\n")

#inFile.close()
#outFile.close()
