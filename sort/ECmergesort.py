"""
This is an implementation of merge sort
from introduction to algorithms, CLRS
I used many resource:
http://love-python.blogspot.com/2013/10/merge-sort-implementation-in-python.html
//www.geeksforgeeks.org/merge-sort/rint(array)
"""
import time
def merge(A,l,m,r):

    inf = 99999999
    L = [] 
    R = []
    L.extend(A[l : m+1])
    R.extend(A[m+1 : r+1])
    L.append(inf) # sentinal card
    R.append(inf) # sadly not = infinity
    i = 0 
    j = 0 
    for k in range(l,r+1):
        if(L[i]<= R[j]):
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1

def mergeSort(A,l,r):
    if l<r:
	m = (l+r)/2
	mergeSort(A,l,m)
	mergeSort(A,m+1,r)
	merge(A,l,m,r)

#main 
nums = input("Number of values: ")
BCArray = []
WCArray = []
for x in range(0, nums):
    BCArray.append(x)

for x in range(nums, 0, -1):
    WCArray.append(x)
length = nums

start_time = time.time()
mergeSort(BCArray,0,length-1)
print("Best case time--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
mergeSort(WCArray,0,length-1)
print("Worst case time --- %s seconds ---" % (time.time() - start_time))
