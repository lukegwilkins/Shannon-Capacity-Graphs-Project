from copy import deepcopy
from graphProduct import graphProductPower
def removeVertexEdges(graph, vertex):
	for i in range(len(graph[vertex])):
		if i!=vertex:
			graph[i][vertex]=0
	graph[vertex]=[0]*len(graph)
		
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
	return vertexCover
			
def indepSetApprox(graph):
	vertexCover=vertexCoverApprox(graph)
	
	indepSet=[]
	for i in range(len(graph)):
		if i not in vertexCover:
			indepSet.append(i)
	return indepSet
matrix=[[1,1,0,0,1], [1,1,1,0,0], [0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]]

test= graphProductPower(matrix,2)
for i in test:
	print(i)
	
indepSet= indepSetApprox(test)

for i in test:
	print(i)

print(indepSet)