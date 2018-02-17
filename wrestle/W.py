"""
This is a modified BFS algorithm to find the rivalry relations between
groups of wrestlers. The user should run the script with input files included.
"""
from sys import argv
from collections import deque
script, inFilename = argv
"""
Class to simulate a vertices in a graph
Holds team affiliation, vertex color and list
of adjacent vertices.
"""
class vertex:
     def __init__(self):
        self.adj = [] 
        self.color = "WHITE"
        self.team = ""
"""
This is a function to determine if a link exists between two
wrestlers. If there is that means that there is a rivalry. A rivalry
cannot exist between babyfaces babyfaces or heels and heels, this relation 
results in failure. 
"""
def babsAndHeels(G, s):
	G[s].team = "baby" 
	G[s].color = "GRAY"
	Q = deque([])
	Q.append(s)
	while Q: 
		u = Q.popleft()
		for v in G[u].adj:
			if G[v].color == "GRAY" and G[v].team == G[u].team:
				return False #If  team types are the same fail
			if G[v].color == "WHITE":
				G[v].color = "GRAY"  #vertex active
				if G[u].team == "baby":
					G[v].team = "heel"
				else:
					G[v].team = "baby"
				Q.append(v)
		G[v].color= "BLACK" #vertex visited
	return True


G = {} 
wArr = []
eArr = []

with open(inFilename, "r") as inFile:
	numW = int(inFile.readline())
	for i in range(0,numW):
		wArr.append(inFile.readline())
	wArr = [x.rstrip() for x in wArr]
	G = dict((x,vertex()) for x in wArr) #Creates dictionary of wrestlers
	numE = int(inFile.readline())		#with vertex objects as values
        for line in range(0, numE):
            edge = inFile.readline().split()
            G[edge[0]].adj.append(edge[1]) #If rivalry exists between a->b
            G[edge[1]].adj.append(edge[0]) # the same exists for b->a

result = True
for key in G:
	if(G[key].color == "WHITE"):
		result = babsAndHeels(G,key)
		if(result == False): # If wrestlers are on same team
			print "Impossible" # the graph is a failure
			break;
if result:
	print "Yes Possible\nBabfaces: ",
	for key in G:
		if G[key].team == "baby":
			print key,
	print"\nHeels: ",
	for key in G:
		if G[key].team == "heel":
			print key,
