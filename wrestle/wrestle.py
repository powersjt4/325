"""
This is an implementation of an activity scheduler 
"""
import itertools
from sys import argv
script, inFilename = argv
#inFile = open(inFilename, "r")
wDict = {}
wArr = []
eArr = []

with open(inFilename, "r") as inFile:
	numW = int(inFile.readline())
	for i in range(0,numW):
		wArr.append(inFile.readline())
	wArr = [x.rstrip() for x in wArr]
	wDict = dict((x,[]) for x in wArr)
	numE = int(inFile.readline())
	for line in range(0, numE):
		edge = inFile.readline().split()
		print edge[0]
		wDict[edge[0]].append(edge[1])
		wDict[edge[1]].append(edge[0])
#print wArr
#print wDict 

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
bfs_connected_component(wDict,'Bear') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
