"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "act.txt"
inFile = open(input, "r")
"""
#Greedy choice is to select the last to start
#A[n][0] = act. # a[n][1] = Start a[n][2] = Finish
def activitySchedule(A,length):
    for i in range(0,int(length)-1): 
        next = A[i+1]
        cur = A[i]
        if(next[1] > cur[1] and next[2] >= cur[1]):
            if(next[2]>=cur[1]):
                print(next)
        elif(cur[1] > prev[1] and cur[2]>=next[2]):
            print(cur)

            #print("Start", A[i][1]," <= start 2",prev[1])
		#f(A[i][1] >= prev[1] and A[i][1]>=prev[2]):#S of next >= f of prev
		#    print(A[i])
                #elif(prev[1] >= A[i][1] and prev[2]>= A[i][1]):
                #    print(prev)    
"""                

 
def activitySchedule(A,length):	
    print(A[0])
    k = 1
    for i in range(1, int(length)):
        if(A[i][2] <= A[k][1]):  
            print(A[i])
            k = i
        
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
# A[i][1] = sort on start time, A[i][2] = sort on finish time    
    for i in range(1, int(arrLen)):
         key = A[i][1]
         prev = A[i] 
         j = i - 1
         while (j >= 0 and key > A[j][1]):# > Desc. < ascend
             A[j+1] = A[j]
             j-= 1
         A[j+1] = prev   
    activitySchedule(A,arrLen)		


    print(A)
    print("\n\n")
inFile.close()

