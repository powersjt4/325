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
		#app = input("Number to append: ")
		outFile.write("\n%d\n"% int(nums/10))
		blocks = blocks- 1
		print(blocks)

#main
output = raw_input("Please name your output file: ")
outFile = open(output, "w+") 
blocks = input("Number of blocks: ")
writeToTxt(outFile,blocks)
print("...results written to",output,".txt")
outFile.close()
