import networkx as nx
def minimumDegreeNode(graph):
	nodes=graph.nodes()
	degrees=graph.degree(nodes)
	minimumNode=(-1,-1)
	for node in degrees:
		if (node[1]<minimumNode[1]) or (minimumNode[0]==-1):
			minimumNode=node
		
	return minimumNode[0]
	
def greedyAlg(graph):
	#print(graph.nodes())
	indepSet=[]
	while len(graph.nodes())!=0:
		#print(graph.nodes())
		minimumNode=minimumDegreeNode(graph)
		indepSet.append(minimumNode)
		#print(minimumNode)
		neighbors=[]
		for i in graph.neighbors(minimumNode):
			neighbors.append(i)
		
		for i in neighbors:
			graph.remove_node(i)
		graph.remove_node(minimumNode)
		#print(len(graph.nodes()))
	return indepSet