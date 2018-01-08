filename = "data.txt"
file = open(filename, "r")
#for line in file:
#   print line,

for line in file:
	n = 0
	for n in line.split(): 
		if n.isdigit():
			print n
	print "new line"

file.close()
