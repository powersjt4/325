def merge(first, second):
	mergedList = []
	while(len(first)>1 and len(second) >1):
		if(first[0] > second[0]):
			mergedList.append(second[0])
			del second[0] 
		else:
			mergedList.append(first[0])
			del first[0]

		if (len(first) < 1):
			mergedList.append(second[0])
		if(len(second) < 1):
			mergedList.append(second[0])
	
	return mergedList

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
