"""
This is an implementation of an activity scheduler 
"""
input = "act.txt"
inFile = open(input, "r")
"""
Recieves a 2D list of values containing(activity #, start, finish),
the length of the array and the number of times the function was called.It outputs the last to start activity  number sorted by start time. 
""" 
def activitySchedule(A,length,set):	
    pArr = [A[0]]
    k = 0 
    for i in range(1, int(length)):
        if(A[k][1]>=A[i][2]):  
            #print(A[i])
            pArr.append(A[i])
            k = i
    pArr = sorted(pArr, key=lambda x: x[1])
    print("Set %d" %set) 
    print("Number of activities selected = %d" %len(pArr)) 
    print("Activities:"),     
    for i in pArr:
        print(i[0]), 

set = 1#tracks the number of value sets
while True:
    A = []
    arrLen = inFile.readline()#Read in length, first line
    if not arrLen: break #EOF breaks loop.
    for lineItem in range(0, int(arrLen)):#Read each line after for arrLen 
        line = inFile.readline()#line is activit #,Start,Finish    
        A.append([])#Creates new line in A 
        for i in line.split():#Splits line into act. #, start, finish
            A[lineItem].append(int(i))#Appends to new row in t and converts to int

#Insertion sort sort whole row by the last value the finish time.
# A[i][1] = sort on start time, A[i][2] = sort on finish time    
    for i in range(1, int(arrLen)):
         key = A[i][1]
         prev = A[i] 
         j = i - 1
         while (j >= 0 and key > A[j][1]):# > Desc. < ascend
             A[j+1] = A[j]
             j-= 1
         A[j+1] = prev   
    activitySchedule(A,arrLen,set)		
    set = set+1
    print("\n\n")
inFile.close()

