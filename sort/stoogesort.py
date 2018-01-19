import math
def StoogeSort(A,l,h):
        if l>=h:
            return
        if (A[l] > A[h]):
            A[l],A[h] = A[h],A[l]
        
        elif (h-l+1 > 2):
	    m = int(math.ceil((h-l+1)/3))
	    StoogeSort(A,l, h-m)
	    StoogeSort(A,l+m,h)
	    StoogeSort(A,l, h-m)
#main
    
array = [2,3,8,6,1,9]

StoogeSort(array,0, len(array)-1)
for x in array:
    print (x)

