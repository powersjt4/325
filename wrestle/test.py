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
    print key +" "+G[key].color
"""
GoodBadGuys(list of wrestlers, pairs of rivalries)
Build an adjacency list representation for G = (V, E) such that each wrestler
corresponds to a vertex in V and each edge in E = (V1, V2) represents a rivalry between
the wrestlers associated with V1 and V2
 for each vertex u is in V [G]
    do color [u] == WHITE
 for each vertex u in in V [G]
    do if color [u] = WHITE
        then guy==BFS-GOOD-BAD(G, u, guy)
 return guy
BFS-GOOD-BAD(G, s, guy)
 color[s] == Gray
 guy[s] == GOOD
 Q == nil 
 ENQUEUE(Q, s)
 while Q not empty 
    do u == DEQUEUE(Q)
        for each v is in Adj[u]
            do if color[v] = GRAY and guy[v] = guy[u]
                then return FAIL
            if color[v] = WHITE
                then color[v] == GRAY
                if guy[u] = GOOD
                    then guy[v] == BAD
                    else guy[v] == GOOD
                ENQUEUE(Q, v)
        color[u] == BLACK
 return guy

print G[key].adj
"""

