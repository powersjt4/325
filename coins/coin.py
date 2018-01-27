"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "amount.txt"
output = "change.txt"

def makeChange(V,A,T,C):
	for i in range (A+1):
		coin = 1
		currentCount = i
		for j in [c for c in V if c <= i]:
	 		if (T[i-j] + 1) < currentCount:
				currentCount = T[i-j]+1
				coin = j
			T[i] = currentCount
			C[i] = coin
	return T[A]


def writeToFile(array, amount, coins):
    for item in array:
        outFile.write("%d "% item)
    outFile.write("\n")
    outFile.write("%d \n" %amount) 
    for coin in coins:
        outFile.write("%d "% coin)
    outFile.write("\n\n")

#main
inFile = open(input, "r")
outFile = open(output, "w") 
while True:
        values = []#Denominations of coins
        line = inFile.readline() 
        if not line: break  # EOF
        amount = int(inFile.readline())#amount to change
        for val in line.split():
            values.append(int(val))
        count = [0]*(amount+1)
        coinTypes = [0]*(amount+1)
        makeChange(values, amount, count, coinTypes) 
        print(amount)
        print(coinTypes)
        print(values)
        writeToFile(values, amount, coinTypes)
inFile.close()
outFile.close()
