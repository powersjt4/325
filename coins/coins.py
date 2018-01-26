"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: https://www.geeksforgeeks.org/insertion-sort/
"""
input = "amount.txt"
output = "change.txt"
"""
V = Denominations of coins, A = Amount of coins to change
T = storesmin number of coins to make amount
C = values of coin types to make amount 
"""

def makeChange(V,A,T,C):
	for j in range(len(V)):
		for i in range(1, A+1):
			cur = V[j]
			if i >= V[j]:
				if T[i] > 1+T[i-cur]:
					T[i] = 1 + T[i-cur]
					C[i] = j
	
	start = len(C)-1				
	while (start > 0): 
		print (V)
		print (C)
		print (T)
		coin = V[C[start]]
		#print "%d "% coin,
		start = start - coin
	return T[A-1] #Return min number of coins

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
        count = [float("inf") for idx in range(amount+1)]#min number of coins to make amount
        coinTypes = [-1 for idx in range(amount + 1)]#Stores values of coin types  
        makeChange(values, amount, count, coinTypes) 
#        print(amount)
#        print(count)
#        print(coinTypes)
#        print(values)
        writeToFile(values, amount, coinTypes)
inFile.close()
outFile.close()


