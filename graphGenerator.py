import networkx as nx

import random
from datetime import datetime

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
	
def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph
	
def probabilisticGraph(n,p):
	graph=nx.complete_graph(n)
	random.seed(datetime.now())
	edges=list(graph.edges())
	
	i=0
	while i<len(edges):
		if(random.random()>p):
			graph.remove_edge(edges[i][0],edges[i][1])
		i+=1
	return graph
		
def starCycleGen(n,m):
	graph=nx.Graph()
	vertex=0
	for i in range(m):
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
	
#print(starCycleGen(4,1).edges())
#print(probabilisticGraph(7,0.15).edges())