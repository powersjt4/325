"""
This is an implementation of an activity scheduler 
"""
import itertools
from sys import argv
from collections import deque
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
G = dict((x,white) for x in wArr)
babs = []
heels = []
Q = deque([])
Q.append(wArr[0])
print Q
while len(Q) != 0:
    u = Q.popleft()
        for x in G[u]  

