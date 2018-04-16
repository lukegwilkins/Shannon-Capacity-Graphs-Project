import random
import networkx as nx
#from networkx.algorithms import approximation
from cliquerAlg import cliquer
from datetime import datetime
random.seed(datetime.now())

"""This function converts a node in a strong graph product graph into a list of integers"""
def nodeConversion(node):
	#if the node is an int then we return a list containing just the node
	if type(node) is int:
		return [node]
	#else we recurse on the left half of the node and the right half of the node
	else:
		left = node[0]
		right = node[1]
		node=nodeConversion(left)+nodeConversion(right)
		return node

"""gets the lee distance between 2 nodes"""
def leeDistance(vOne,vTwo,p):
	distance=0	
	if(type(vOne) is int):
		difference = abs(vOne-vTwo)
		if(difference<(p-difference)):
			distance+=difference
		else:
			distance +=p-difference
	else:
		#converts the nodes
		vOneConv=nodeConversion(vOne)
		vTwoConv=nodeConversion(vTwo)
		
		#calcualtes the lee distance
		for i in range(len(vOne)):
			difference = abs(vOneConv[i]-vTwoConv[i])
			if(difference<(p-difference)):
				distance+=difference
			else:
				distance +=p-difference
	return distance

"""gets all the nodes in the independent set at a distance greater than b from vertex"""
def distanceVertices(indepSet, vertex, b, p):
	returnList=[]
	for i in indepSet:
		if(leeDistance(i,vertex, p)>b):
			returnList.append(i)
	return returnList

"""gets the graph with the neighbours of any vertex in vertices removed"""
def graphWithNeighborsRemoved(graph, vertices):
	#creates a copy of graph
	returnGraph = graph.copy()
	for i in vertices:
		neighbors =[]
		for j in returnGraph.neighbors(i):
			neighbors.append(j)
		#print(neighbors)
		for j in neighbors:
			returnGraph.remove_node(j)
		
		returnGraph.remove_node(i)
	return returnGraph

"""Gets the union of 2 lists"""
def unionList(listA, listB):
	for i in listB:
		if i not in listA:
			listA.append(i)
	return listA

"""This function performs the stochastic search"""	
def search(graph, b, p, k):
	#gets the initial independent set
	indepSet=greedyAlg(graph.copy())
	indepSetBest=indepSet
	condition=True
	count=0
	while condition:
		#gets a random vertex from the independent set and removes it and any vertices too close to it in the independent set
		i = indepSet[random.randint(0,len(indepSet)-1)]
		indepSetLoop=distanceVertices(indepSet, i, b, p)
		
		#gets the subgraph of vertices which could be added to the reduced independent set
		subGraph=graphWithNeighborsRemoved(graph,indepSetLoop)
		subGraph.remove_node(i)
		print(len(subGraph.nodes()))
		
		#gets the maximum independent set in the subgraph and adds it to the independent set
		maxInd=cliquer(nx.complement(subGraph))
		indepSet= unionList(indepSetLoop,maxInd)
		
		#if the new independent set is better we store it
		if(len(indepSet)>len(indepSetBest)):
			indepSetBest=indepSet
		
		#increases count
		count+=1
		print(count)
		#if the termination condition is met then we stop looping
		iters=100
		if(count>iters):
			condition=False
	#returns the best independent set
	return indepSetBest

"""Function to return the minimum degree node"""
def minimumDegreeNode(graph):
	nodes=graph.nodes()
	degrees=graph.degree(nodes)
	minimumNode=(-1,-1)
	for node in degrees:
		if (node[1]<minimumNode[1]) or (minimumNode[0]==-1):
			minimumNode=node
		
	return minimumNode[0]

"""Function to return the independent set calculated by the greedy algorithm"""	
def greedyAlg(graph):
	indepSet=[]
	while len(graph.nodes())!=0:
		minimumNode=minimumDegreeNode(graph)
		indepSet.append(minimumNode)
		neighbors=[]
		for i in graph.neighbors(minimumNode):
			neighbors.append(i)
		
		for i in neighbors:
			graph.remove_node(i)
		graph.remove_node(minimumNode)
	return indepSet

