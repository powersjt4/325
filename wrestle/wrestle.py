"""
This is an implementation of an activity scheduler 
"""
import itertools
from sys import argv
script, inFilename = argv
#inFile = open(inFilename, "r")
G = {}
wArr = []
eArr = []

with open(inFilename, "r") as inFile:
	numW = int(inFile.readline())
	for i in range(0,numW):
		wArr.append(inFile.readline())
	wArr = [x.rstrip() for x in wArr]
	G = dict((x,[]) for x in wArr)
	numE = int(inFile.readline())
	for line in range(0, numE):
		edge = inFile.readline().split()
		print edge[0]
		G[edge[0]].append(edge[1])
		G[edge[1]].append(edge[0])
#print wArr
#for key in G:
#    G[key].append([0,2])
print G['Duke'] 
"""
New plan create the BFS but add the key of the baby or heel to
a seperate list.
"""