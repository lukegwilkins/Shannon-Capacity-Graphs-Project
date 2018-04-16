import networkx as nx

"""This gets the smallest degree node in the graph"""
def minimumDegreeNode(graph):
	nodes=graph.nodes()
	#get the nodes and their degrees
	degrees=graph.degree(nodes)
	
	#loop through the nodes and finds the one with the smallest degree
	minimumNode=(-1,-1)
	for node in degrees:
		if (node[1]<minimumNode[1]) or (minimumNode[0]==-1):
			minimumNode=node
		
	return minimumNode[0]

"""This function returns the independent set made by the greedy algorithm"""
def greedyAlg(graph):
	indepSet=[]
	while len(graph.nodes())!=0:
		#gets the node with the smallest degree and adds it to the independent set
		minimumNode=minimumDegreeNode(graph)
		indepSet.append(minimumNode)
		
		#removes its neighbors
		neighbors=[]
		for i in graph.neighbors(minimumNode):
			neighbors.append(i)
		
		for i in neighbors:
			graph.remove_node(i)
		graph.remove_node(minimumNode)
	return indepSet