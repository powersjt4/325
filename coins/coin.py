"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "amount.txt"
output = "change.txt"
def makeChange(values,chgAmount, count, coinTypes):
	for i in range (chgAmount+1):
		coin = 1
		currentCount = i
		for j in [c for c in values if c <= i]:
	 		if (count[i-j] + 1) < currentCount:
				currentCount = count[i-j]+1
				coin = j
			count[i] = currentCount
			coinTypes[i] = coin
	return count[chgAmount]
def writeToFile(array, amount, coins):
    for item in array:
        outFile.write("%d "% item)
    outFile.write("\n")
    outFile.write("%d \n" %amount) 
        
#main
inFile = open(input, "r")
outFile = open(output, "w")
while True:
        array = []
        line = inFile.readline() 
        if not line: break  # EOF
        amount = int(inFile.readline())
        for val in line.split():
            array.append(int(val))
        print(amount)
        print(isinstance(amount, int))
        print(array)
        writeToFile(array, amount, array)
inFile.close()
outFile.close()
