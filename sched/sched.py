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
#Insertion sort
    for i in range(1, int(arrLen)):
        key = list[i][2]
        prev = list[i] 
        j = i - 1
        while (j >= 0 and key < list[j][2]):
            list[j+1] = list[j]
            j-= 1
        list[j+1] = prev 

    print(list)

    print("\n\n")
inFile.close()

