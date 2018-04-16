import networkx as nx

"""Gets the vertex with the maximum degree"""	
def maxDegreeVertex(graph, usableVertices):
	maxVertex=usableVertices[0]
	maxDegree=graph.degree(maxVertex)
	
	for i in usableVertices:
		degree=graph.degree(maxVertex)
		if(degree>maxDegree):
			maxVertex=i
			maxDegree=degree
	return maxVertex

"""Gets the vertex ordering based on graph colouring"""	
def graphColouringOrder(graph):
	#gets the vertices and edges
	uncolouredVertices=list(graph.nodes())
	edges=list(graph.edges())
	vertexOrdering=[]
	colouring=[[]]
	
	#it the colours the graph using the greedy algorithm
	while(len(uncolouredVertices)>0):
		#gets the uncoloured vertex with the maximum degree
		vertexToColour=maxDegreeVertex(graph, uncolouredVertices)
		vertexOrdering.append(vertexToColour)
		newColourClass=True
		
		#gets the vertex's colour
		i=0
		while i<len(colouring):
			addToColourClassI=True
			j=0
			while j<len(colouring[i]):
				if (colouring[i][j], vertexToColour) in edges:
					addToColourClassI=False
					j=len(colouring[i])+1
				j+=1
			
			if(addToColourClassI):
				colouring[i].append(vertexToColour)
				newColourClass=False
				i=len(colouring)+1
			
			i+=1
		
		#if a new colour class is required we create it
		if(newColourClass):
			temp=[]
			temp.append(vertexToColour)
			colouring.append(temp)
			
		uncolouredVertices.remove(vertexToColour)
	return vertexOrdering
			