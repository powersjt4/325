"""
This is an implementation of merge sort
from introduction to algorithms, CLRS
Other resources:
http://love-python.blogspot.com/2013/10/merge-sort-implementation-in-python.html
//www.geeksforgeeks.org/merge-sort/rint(array)
"""
import time
import random 
           #p q r
def merge(A,l,m,r):
#    n1 = m-l+1 
#    n2 = r-m
    inf = 99999999
    L = [] 
    R = []
    L.extend(A[l : m+1])
    R.extend(A[m+1 : r+1])
    L.append(inf) # sentinal card
    R.append(inf) # = infinity
    i = 0 
    j = 0 
   # k = l 
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
nums = input("Number of random values: ")
array = []
for x in range(nums):
    array.append(random.randint(0,10000))
length = nums


start_time = time.time()
mergeSort(array,0,length-1)
print("--- %s seconds ---" % (time.time() - start_time))
