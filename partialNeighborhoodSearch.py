import random
import networkx as nx
from datetime import datetime
random.seed(datetime.now())

def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph

def graphStrongProdPower(graph,k):
	binaryOfK=bin(k)[2:]
	resultingGraph="empty"
	currentProdGraph=graph
	#print(binaryOfK)
	for i in range(len(binaryOfK)-1,-1,-1):
		if(binaryOfK[i]=='1'):
			if(resultingGraph=="empty"):
				resultingGraph=currentProdGraph
			else:
				resultingGraph=nx.strong_product(graph,currentProdGraph)
		
		if(i>0):
			currentProdGraph=nx.strong_product(currentProdGraph,currentProdGraph)
	return resultingGraph

def nodeConversion(node):
	left=node[0]
	right=node[1]
	node=[node[1]]
	while type(left) is tuple:
		node=[left[1]]+node
		left=left[0]
	node=[left]+node
	return node
	
def search(graph, b):
	indepSet=greedyIndepSet(graph)
	indepSetLoop=indepSet
	while True:
		i = indepSet[random.randint(0,len(indepSet)-1)]
		indepSetLoop=distanceVertices(indepSet, i, b)
		subGraph=graphWithNeighborsRemoved(graph,indepSetLoop)
		#subgraph remove i
		maxInd=maxIndSet(subGraph, graph)
		indepSet= unionList(indepSetLoop,maxInd)
		if(len(indepSet)>len(indepSetLoop)):
			indepSetLoop=indepSet

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
	return indepSet

k=2
indepSet=greedyAlg(graphStrongProdPower(cycleGenerator(7),k))
print(indepSet)
print(len(indepSet))
print(len(indepSet)**(1/k))

print()
print(nodeConversion(((1,2),3)))