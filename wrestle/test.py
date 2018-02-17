"""
This is a test file to see if tuples are the way to go
"""
import itertools
from sys import argv
from collections import deque
script, inFilename = argv

class vertex:
     def __init__(self):
        self.adj = [] 
        self.color = "WHITE"
        self.team = "baby"
G = {} 
wArr = []
eArr = []

with open(inFilename, "r") as inFile:
	numW = int(inFile.readline())
	for i in range(0,numW):
		wArr.append(inFile.readline())
	wArr = [x.rstrip() for x in wArr]
	G = dict((x,vertex()) for x in wArr)
	numE = int(inFile.readline())
        for line in range(0, numE):
            edge = inFile.readline().split()
            G[edge[0]].adj.append(edge[1])
            G[edge[1]].adj.append(edge[0])
for key in G:
    if(G[key].color=="WHITE"):
        Q = deque([])
        Q.append(key)
        while len(Q) != 0:
            u = Q.popleft()
            for v in G[u].adj:
                if G[v].color == "GRAY" and v == u:
                    print "Failure!"
                if G[v].color == "WHITE":
                    G[v].color = "GRAY"
                    if G[u].team == "baby":
                        G[v].team = "heel"
                    else:
                        G[v].team = "baby"
                    Q.append(v)
            G[v].color= "BLACK"
for key in G:
    print key +" "+G[key].team
"""
print G[key].adj
"""

