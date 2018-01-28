import time

"""
This is an implementation of insertion sort
from introduction to algorithms, CLRS
Other resources: 
http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
"""
input = "amount.txt"
output = "change.txt"
"""
Modeled after code found in link above and pseudocode
recieves all arrays and amounts by reference.
"""
def makeChange(V,A,T,C):
    for i in range (A+1): #loop through amount
        coin = 1 
        count = i
        for j in [c for c in V if c <= i]:#filters values to to less than current
            if (T[i-j] + 1) < count:
                count = T[i-j]+1
                coin = j
            T[i] = count
            C[i] = coin
"""
Writes all the information to the output file 
calculates the denomenations used and creates a new array
for track coin use.
"""
def writeToFile(array, amount, coins, count, timer):
    for item in array:
        outFile.write("%d "% item)
    outFile.write("\n")
    outFile.write("%d \n" %amount) 
    coin = amount 
    coinCnt = [0]*len(array)#Array same size as original denomenations
    while coin > 0:
        current = coins[coin]
        for i in range(len(array)):
            if(array[i] == current): #Searches array to find instance of current
                coinCnt[i]+=1 
        coin = coin - current #Subtracts current value to get next value
    for item in coinCnt:
        outFile.write("%d "% item)
    
    outFile.write("\n%d "% count[amount])
    outFile.write("\nThis is time ->%s "% timer)
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
        start_time = time.time()
        makeChange(values, amount, count, coinTypes) 
        timer = time.time() - start_time
        writeToFile(values, amount, coinTypes, count, timer)

print("...results written to changes.txt")
inFile.close()
outFile.close()
