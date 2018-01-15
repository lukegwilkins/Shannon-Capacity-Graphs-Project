import networkx as nx

def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph
	
def maxDegreeVertex(graph, usableVertices):
	maxVertex=usableVertices[0]
	maxDegree=graph.degree(maxVertex)
	
	for i in usableVertices:
		degree=graph.degree(maxVertex)
		if(degree>maxDegree):
			maxVertex=i
			maxDegree=degree
	return maxVertex
	
def graphColouringOrder(graph):
	uncolouredVertices=list(graph.nodes())
	edges=list(graph.edges())
	vertexOrdering=[]
	colouring=[[]]
	
	while(len(uncolouredVertices)>0):
		#print(uncolouredVertices)
		vertexToColour=maxDegreeVertex(graph, uncolouredVertices)
		vertexOrdering.append(vertexToColour)
		newColourClass=True
		
		i=0
		while i<len(colouring):
			#neighbors=list(graph.neighbors(vertexToColour))
			addToColourClassI=True
			#print(i)
			#print("here")
			j=0
			#print(neighbors)
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
		if(newColourClass):
			temp=[]
			temp.append(vertexToColour)
			colouring.append(temp)
			
		uncolouredVertices.remove(vertexToColour)
		#print(colouring)
	return vertexOrdering
			

#cycle=cycleGenerator(9)
#print(graphColouringOrder(cycle))