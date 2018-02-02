"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "act.txt"
inFile = open(input, "r")

while True:
    list = []
    arrLen = inFile.readline()
    if not arrLen: break #EOF 
    for lineItem in range(0, int(arrLen)): 
        line = inFile.readline()    
        list.append([])
        for i in line.split():
            list[lineItem].append(int(i))
    print(list)
    print("\n\n")
inFile.close()
