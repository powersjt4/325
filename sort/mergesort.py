input = "data.txt"
output = "merge.out"
inFile = open(input, "r")
outFile = open(output, "w")

for line in inFile:
        array = [] 
        for val in line.split():
            array.append(int(val))
		length = int(array[0]) 
        array.pop(0)
        print len(array)
		
			
	
        print(array)
        for item in array:
            outFile.write("%d "% item)
        outFile.write("\n")

inFile.close()
outFile.close()

#MERGE-SORT A[1 . . n]
#1.If n = 1, done.
#2.Recursively sort A[ 1 . . n/2 ] and A[ n/2+1 . . n ] .
#3.“Merge” the 2 sorted lists.


def merge(first, second):
	mergedList = []
	while(len(first)>1 and len(second) >1)
		if(first[0] > second[0])
			mergedList.append(second[0])
			del second[0] 
		else:
			mergedList.append(first[0])
			del first[0]

		if len(first) < 1
			mergedList.append(second[0])
		else:
			mergedList.append(first[0])
	
	return mergedList
