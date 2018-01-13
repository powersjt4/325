"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "data.txt"
output = "insert.out"
inFile = open(input, "r")
outFile = open(output, "w")

for line in inFile:
        array = [] 
        for val in line.split():
            array.append(int(val))
	length = int(array[0]) 
        array.pop(0)
        print len(array)

        for i in range(1,length): 
            cur = array[i]
            prev = i-1 
            while prev >=0 and cur < array[prev] :
                array[prev+1] = array[prev]
                prev -= 1
            array[prev+1] = cur
        print(array)
        for item in array:
            outFile.write("%d "% item)
        outFile.write("\n")

inFile.close()
outFile.close()
