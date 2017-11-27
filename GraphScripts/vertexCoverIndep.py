from copy import deepcopy
import random
from datetime import datetime
#from graphProduct import graphProductPower
def removeVertexEdges(graph, vertex):
	for i in range(len(graph[vertex])):
		if i!=vertex:
			graph[i][vertex]=0
	graph[vertex]=[0]*len(graph)
	
def vertexCoverApprox(graph):
	random.seed(datetime.now())
	edges=[]
	for i in graph.edges():
		edges.append(i)
	vertexCover=[]
	#print(edges)
	#print(edges[0])
	while(edges !=[]):
		randomEdge=random.randint(0,len(edges)-1)
		#print(randomEdge)
		edge = edges[randomEdge]
		#print(edge)
		vertexCover.append(edge[0])
		vertexCover.append(edge[1])
		removeEdges(edges,edge[0])
		removeEdges(edges,edge[1])
		#print(edges)
	#print(vertexCover)
	print(len(vertexCover))
	#print(edges)

def removeEdges(edges,vertex):
	i=0
	while i<len(edges):
		if(edges[i][0]==vertex or edges[i][1]==vertex):
			del edges[i]
		else:
			i+=1
""""
def vertexCoverApprox(graph):
	graphCopy=deepcopy(graph)
	vertexCover=[]
	edgesLeft=True
	
	while(edgesLeft):
		edgesLeft=False
		i=0
		while i<len(graphCopy):
			j=0
			while j<len(graphCopy):
				if i!=j:
					if graphCopy[i][j]==1:
						vertexCover.append(i)
						#vertexCover.append(j)
						
						removeVertexEdges(graphCopy, i)
						#removeVertexEdges(graphCopy, j)
						
						i+=1
						j=len(graphCopy)
						edgesLeft=True
				j+=1
			i+=1
	#print(vertexCover)
	return vertexCover
"""		
def indepSetApprox(graph):
	vertexCover=vertexCoverApprox(graph)
	
	indepSet=[]
	for i in range(len(graph)):
		if i not in vertexCover:
			indepSet.append(i)
	return indepSet
""""matrix=[[1,1,0,0,1], [1,1,1,0,0], [0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]]

test= graphProductPower(matrix,2)
for i in test:
	print(i)
	
indepSet= indepSetApprox(test)

for i in test:
	print(i)

print(indepSet)"""