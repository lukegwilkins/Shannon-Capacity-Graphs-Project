import networkx as nx
import numpy as np
import random
from datetime import datetime

"""Function to figure out the strong graph product power of a graph"""
def graphStrongProdPower(graph,k):
	#we get the binary representation of k
	binaryOfK=bin(k)[2:]
	resultingGraph="empty"
	currentProdGraph=graph
	
	#we go through and figure out which powers of 2 of the graph we need to get to figure out the strong graph product power 
	for i in range(len(binaryOfK)-1,-1,-1):
		if(binaryOfK[i]=='1'):
			if(resultingGraph=="empty"):
				resultingGraph=currentProdGraph
			else:
				resultingGraph=nx.strong_product(resultingGraph,currentProdGraph)
		
		if(i>0):
			currentProdGraph=nx.strong_product(currentProdGraph,currentProdGraph)
	return resultingGraph

"""Generates a cycle graph of size n"""
def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph

"""Generates a graph of size n with each edge having a probability of p of existing"""	
def probabilisticGraph(n,p):
	graph=nx.complete_graph(n)
	random.seed(datetime.now())
	edges=list(graph.edges())
	
	i=0
	#for each edge we roll a random number, if it is larger than p then we remove that edge
	while i<len(edges):
		if(random.random()>p):
			graph.remove_edge(edges[i][0],edges[i][1])
		i+=1
	return graph

"""Function that returns a list of neighbours for a vertex in a graph which have a degree greater than k"""
def neighborsToRemove(graph, vertex, k):
	removableNeighbors=[]
	for i in graph.neighbors(vertex):
		if graph.degree(i)>k:
			removableNeighbors.append(i)
	return removableNeighbors

"""Function that generates a random regular graph with n nodes and degree k"""
def regularGraph(n,k):
	if(n*k %2==0):
		return nx.random_regular_graph(k,n)
	elif(k>0 and k<n):
		return nx.random_regular_graph(k+1,n)
	else:
		return nx.random_regular_graph(k-1,n)
		
"""Generates a graph which i call a star cycle graph, it creates a cyle graph of size n and adds m nodes which are attached to all nodes in the cycle"""			
def starCycleGen(n,m):
	graph=nx.Graph()
	vertex=0
	#creates the cycle
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		vertex+=1
	
	#print(graph.edges())
	for i in range(m):
		for j in range(n):
			graph.add_edge(vertex,i)
			graph.add_edge(i,vertex)
			vertex+=1
	return graph

"""Generates a random cograph"""
def cograph(n):
	random.seed(datetime.now())
	cographs=[]
	complementGraphs=[]
	
	#we make n graphs consisting of just a node
	for i in range(n):
		graph=nx.Graph()
		graph.add_node(i)
		cographs.append(graph)
	
	#we pick 2 graphs at random
	indexOne=random.randint(0,len(cographs)-1)
	indexTwo=random.randint(0,len(cographs)-1)
	while(indexTwo==indexOne):
		indexTwo=random.randint(0,len(cographs)-1)
	
	#we merge these 2 graphs
	unionGraph=nx.disjoint_union(cographs[indexOne], cographs[indexTwo])
	
	if(indexOne<indexTwo):
		cographs[indexOne]=unionGraph
		del cographs[indexTwo]
	else:
		cographs[indexTwo]=unionGraph
		del cographs[indexOne]
	
	#no we randomly pick 2 options until we have merged all the graphs, we either merge 2 graphs or get the complement of one
	while(len(cographs)>1):
		#rolls a random number to decide if we get the complement or merge 2 graphs
		operationChoice=random.randint(0,4)
		
		#if the number was less than 4 then we get the complement of a random graph
		if(operationChoice<4):
			#we replace the graph with its complement and store which graph we replaced, so we don't get stuck replacing the same graph
			#over and over again
			if(len(complementGraphs)<len(cographs)):
				index=random.randint(0,len(cographs)-1)
				while(index in complementGraphs):
					index=random.randint(0,len(cographs)-1)
				
				complement= nx.complement(cographs[index])
				
				cographs[index]= complement
				complementGraphs.append(index)
		
		#else we merge 2 random graphs
		else:
			indexOne=random.randint(0,len(cographs)-1)
			indexTwo=random.randint(0,len(cographs)-1)
			while(indexTwo==indexOne):
				indexTwo=random.randint(0,len(cographs)-1)
	
			unionGraph=nx.disjoint_union(cographs[indexOne], cographs[indexTwo])
			
			if(indexOne<indexTwo):
				cographs[indexOne]=unionGraph
				del cographs[indexTwo]
			else:
				cographs[indexTwo]=unionGraph
				del cographs[indexOne]
			
			complementGraphs=[]
	
	#finally we roll to decide if we will replace the graph with its complement or not
	complementChoice=random.randint(0,4)
	if(complementChoice<4):
		return nx.complement(cographs[0])
	return cographs[0]

"""generates the graph which I call c6 cross"""
def stronglyRegularC6Cross():
	graph=nx.Graph()
	n=6
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
	return graph

"""generates the graph which I call c6 star"""
def stronglyRegularC6Star():
	graph=nx.Graph()
	n=6
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+2)%n)
		graph.add_edge((i-2)%n,i)
	return graph

"""generates the graph which I call c8 star"""
def stronglyRegularC8Star():
	graph=nx.Graph()
	n=8
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
	return graph

"""generates the graph which I call c8 dense"""
def stronglyRegularC8Dense():
	graph=nx.Graph()
	n=8
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
		graph.add_edge(i,(i+2)%n)
	return graph

"""Generates the paley graph of size 9"""
def paleyGraph9():
	graph=nx.Graph()
	n=9
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i+2)%n,i)
		graph.add_edge(i,(i+4)%n)
		
	return graph

"""Generates the paley graph of size 13"""
def paleyGraph13():
	n=13
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		#graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
		graph.add_edge(i,(i+4)%n)
	return graph

"""Generates the paley graph of size 17"""
def paleyGraph17():
	n=17
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i+2)%n,i)
		graph.add_edge(i,(i+4)%n)
		graph.add_edge(i,(i+8)%n)
	return graph

"""Generates the paley graph of size 25"""
def paleyGraph25():
	#The adjacency matrix was obtained from http://www.distanceregular.org/graphs/paley25.html accessed on 06/04/2018
	adjMatrix=[[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
			   [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
			   [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
			   [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
			   [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
			   [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
			   [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
			   [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
			   [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
			   [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
			   [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
			   [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
			   [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
			   [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
			   [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
			   [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
			   [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
			   [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
			   [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
			   [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
			   [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
			   [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
			   [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
			   [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
			   [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]]
	
	adjMatrix=np.matrix(adjMatrix)
	graph=nx.from_numpy_matrix(adjMatrix)
	return graph
