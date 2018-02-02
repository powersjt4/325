"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "act.txt"
inFile = open(input, "r")

#A[n][0] = act. # a[n][1] = Start a[n][2] = Finish
def activitySchedule(A,length):
	for i in range(1,int(length)): 
		prev = A[i-1]
#		print(A[i][1])
#		print( A[i-1][2])
	
		if(A[i][1] <= A[i-2][2] ):#S of next >= f of prev
			print(A[i])
	

while True:
    A = []
    arrLen = inFile.readline()#Read in length, first line
    if not arrLen: break #EOF 
    for lineItem in range(0, int(arrLen)):#Read each line after for arrLen 
        line = inFile.readline()#line is activit #,Start,Finish    
        A.append([])#Creates new line in A 
        for i in line.split():#Splits line into act. #, start, finish
            A[lineItem].append(int(i))#Appends to new row in t and converts to int

    print(A)
#Insertion sort sort whole row by the last value the finish time.
    for i in range(1, int(arrLen)):
        key = A[i][2]
        prev = A[i] 
        j = i - 1
        while (j >= 0 and key < A[j][1]):
            A[j+1] = A[j]
            j-= 1
        A[j+1] = prev 
	activitySchedule(A,arrLen)		


    print(A)

    print("\n\n")
inFile.close()

