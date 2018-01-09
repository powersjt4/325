#MERGEi(A; p; q; r) where A is an array and p, q, and r are indices into the array
# such that p  q < r.
def merge(first, second):
Merge(A,p,q,r)
	n1 = q-p+1 #find mid point 
	n2 = r- q
	L = [] # Left array
	R = [] # Right array
	
	for i = 1 to n1
		L[i] = A[p+i-1]

	for j = 1 to n2
		R[j] = A[1+j]
	L[n1 +1] = inf # sentinal card
	R[n2 +1] = inf # = infinity

	i = 1
	j= 1
	for k = p to r
		if(L[i]<= R[j])
			A[k] = L[i]
			i = i+1
		else: 
			A[k] = R[j]
			j = j+1
 
	return mergedList

Merge-Sort(A,p,r)
	q = floor(p+r/2)
	Merege-sort(A,p,q)
	Merge-sort (A,q+1,r)
	Merge(A,p,q,r)
 


def mergeSort(arr):
#base case
	if(len(arr)<2):
		return arr
#recursive case
	mid = len(arr)/2
	arrT = mergeSort(arr[:mid])
	arrB = mergeSort(arr[mid:])
	
	return merge(arrT, arrB)

#main 
input = "data.txt"
output = "merge.out"
inFile = open(input, "r")
outFile = open(output, "w")

for line in inFile:
        array = [] 
        for val in line.split():
            array.append(int(val))
	#	length = int(array[0]) 
        array.pop(0)
        print len(array)
        print(mergeSort([3,4,5,1,2,8,3,7,6]))
        for item in array:
            outFile.write("%d "% item)
        outFile.write("\n")

inFile.close()
outFile.close()
