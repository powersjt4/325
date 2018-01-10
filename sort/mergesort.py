           #p q r
def merge(A,l,m,r):
    n1 = m-l+1 
    n2 = r-m
    inf = 9999999
    L = [0] * (n1)
    R = [0] * (n2)
    #Copy array into L and R	
    for i in range(0, n1): 
        L[i] = A[l+i]

    for j in range(0, n2): 
       R[j] = A[m+1+j]
                
    L.append(inf) # sentinal card
    R.append(inf) # = infinity

    i = 1 
    j = 1 
    k = l 

    for k in A:
        if(L[i]<= R[j]):
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1

"""
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
"""
def mergeSort(A,l,r):
    if l<r:
	m = (l+(r-1))/2
	mergeSort(A,l,m)
	mergeSort(A,m+1,r)
	merge(A,l,m,r)
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
