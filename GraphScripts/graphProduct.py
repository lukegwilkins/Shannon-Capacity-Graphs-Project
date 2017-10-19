##make sure to rename so everything makes sense
##do comments

def verticesInGraphProduct(noOfVertices,power):
	vertices=[]
	for i in range(noOfVertices):
		vertices.append(i)
	return verticesInGraphRec(vertices, power)
		
def verticesInGraphRec(vertices, power):
	if power <=1:
		returnList=[]
		for v in vertices:
			returnList.append(str(v))
		return returnList
	else:
		subSequence = verticesInGraphRec(vertices, power-1)
		newVertices=[]
		for v in vertices:
			for sequence in subSequence:
				newVertices.append(str(v)+","+sequence)
		return newVertices


def adjacencyMatrix(vertices, originalGraph):
    adjacencyMatrix=[]
    for i in range(len(vertices)):
        adjacency=[]
        for j in range(len(vertices)):
            if i==j:
                adjacency.append(1)
            else:
                verticesInVertex = vertices[i].split(",")
                verticesInCandidate = vertices[j].split(",")
                adjacent = True
                for k in range(len(verticesInVertex)):
                    if originalGraph[int(verticesInVertex[k])][int(verticesInCandidate[k])]==0:
                        adjacent = False
                if adjacent:
                    adjacency.append(1)
                else:
                    adjacency.append(0)

        adjacencyMatrix.append(adjacency)
                  
    return adjacencyMatrix

def graphProductPower(graph, power):	
	newVertices=verticesInGraphProduct(len(graph),power)
	adjMatrix=adjacencyMatrix(newVertices, graph)
	return adjMatrix
	
""""vertices=[0,1,2]
newVertices=verticesInGraphProduct(3,2)
print(newVertices)
originalGraph=[[1,1,0],[1,1,0],[0,0,1]]
print(adjacencyMatrix(newVertices, originalGraph))

print(graphProductPower(originalGraph, 2))"""