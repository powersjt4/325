           #p q r
def merge(A,l,m,r):
        n1 = m-l+1 
        n2 = r-m
        inf = 9999999
	L = [0] * (n1) # Left array
	R = [0] * (n2) # Right array
        #Copy array into L and R	
        
        for i in range(0, n1): 
		L[i] = A[l+i]

        for j in range(0, n2): 
		R[j] = A[m+1+j]
                
	L.append(inf) # sentinal card
	R.append(inf) # = infinity

	i = 0 
	j = 0 
        k = l 
        while i<n1 and j<n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i+=1
            else:
                A[k] = R[j]
                j +=1
            k+=1
    # Copy the remaining elements of L[], if there
    # are any
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1
     
    # Copy the remaining elements of R[], if there
    # are any
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1
 
def mergeSort(A,l,r):
    if l<r:
	m = (l+(r-1))/2
	mergeSort(A,l,m)
	mergeSort(A,m+1,r)
	merge(A,l,m,r)

"""
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),
 
mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
"""
#main 
input = "data.txt"
output = "merge.out"
inFile = open(input, "r")
outFile = open(output, "w")

for line in inFile:
        array = [] 
        for val in line.split():
            array.append(int(val))
	length = array.pop(0) 
        print length
        mergeSort(array,0,length-1)
        print(array)
        for item in array:
            outFile.write("%d "% item)
        outFile.write("\n")
inFile.close()
outFile.close()
