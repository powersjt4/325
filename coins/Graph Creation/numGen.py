"""
Creates random numbers and prints them to a text file that you name. 
It asks for the number of random values then appends another value to
the bottom of the list. It will perform this for as many number of 
blocks a specified This is to be used with a change making app, so 
the first two numbers in the array are 1 and 2.

Type "python numGen.py" into terminal to run.
"""
import random 
def writeToTxt(outFile, blocks):
	while blocks > 0:	
		nums = input("Number of random values: ")
		array = [1,2]
		for x in range(2,nums):
			array.append(random.randint(0,10000))
		length = nums
		for item in array:
			outFile.write("%d "% item)
		app = input("Number to append: ")
		outFile.write("\n%d\n"% app)
		blocks = blocks- 1
		print(blocks)

#main
output = raw_input("Please name your output file: ")
outFile = open(output, "w+") 
blocks = input("Number of blocks: ")
writeToTxt(outFile,blocks)
print("...results written to",output)
outFile.close()
