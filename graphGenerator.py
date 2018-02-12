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

def neighborsToRemove(graph, vertex, k):
	removableNeighbors=[]
	for i in graph.neighbors(vertex):
		if graph.degree(i)>k:
			removableNeighbors.append(i)
	return removableNeighbors

def regularGraph(n,k):
	if(n*k %2==0):
		return nx.random_regular_graph(k,n)
	elif(k>0 and k<n):
		return nx.random_regular_graph(k+1,n)
	else:
		return nx.random_regular_graph(k-1,n)
		
			
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

def cograph(n):
	random.seed(datetime.now())
	cographs=[]
	complementGraphs=[]
	for i in range(n):
		graph=nx.Graph()
		graph.add_node(i)
		cographs.append(graph)
		#complementableGraphs.append(-1)
		#print(graph.nodes())
	#print(cographs)
	#print(complementableGraphs)
	
	indexOne=random.randint(0,len(cographs)-1)
	indexTwo=random.randint(0,len(cographs)-1)
	while(indexTwo==indexOne):
		indexTwo=random.randint(0,len(cographs)-1)
	
	unionGraph=nx.disjoint_union(cographs[indexOne], cographs[indexTwo])
	#print(indexOne, indexTwo)
	if(indexOne<indexTwo):
		cographs[indexOne]=unionGraph
		del cographs[indexTwo]
	else:
		cographs[indexTwo]=unionGraph
		del cographs[indexOne]
		
	while(len(cographs)>1):
		operationChoice=random.randint(0,4)
		
		if(operationChoice<4):
			if(len(complementGraphs)<len(cographs)):
				index=random.randint(0,len(cographs)-1)
				while(index in complementGraphs):
					index=random.randint(0,len(cographs)-1)
				
				complement= nx.complement(cographs[index])
				
				cographs[index]= complement
				complementGraphs.append(index)
				
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
	print(cographs)		
	for i in cographs:
		print(i.nodes())
	
	complementChoice=random.randint(0,4)
	if(complementChoice<4):
		return nx.complement(cographs[0])
	return cographs[0]

def stronglyRegularC6Cross():
	graph=nx.Graph()
	n=6
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
	return graph

def stronglyRegularC6Star():
	graph=nx.Graph()
	n=6
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+2)%n)
		graph.add_edge((i-2)%n,i)
	return graph

def stronglyRegularC8Star():
	graph=nx.Graph()
	n=8
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
	return graph

def stronglyRegularC8Dense():
	graph=nx.Graph()
	n=8
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
		graph.add_edge(i,(i+2)%n)
	return graph

def stronglyRegularC9Bipartite():
	graph=nx.Graph()
	n=9
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		
	graph.add_edge(0,7)
	graph.add_edge(0,5)
	
	graph.add_edge(1,3)
	graph.add_edge(1,5)
	
	graph.add_edge(2,7)
	graph.add_edge(2,6)
	
	graph.add_edge(3,8)
	
	graph.add_edge(4,8)
	graph.add_edge(4,6)
	return graph

def paleyGraph():
	n=13
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		graph.add_edge(i,(i+3)%n)
		graph.add_edge(i,(i+4)%n)
	return graph
	
#print(starCycleGen(4,1).edges())
#print(probabilisticGraph(7,0.15).edges())
#print(regularGraph(7,4).edges())
#print(cograph(7).edges())
#print(stronglyRegularC9Bipartite().edges())
#print(nx.is_strongly_regular(stronglyRegularC9Bipartite()))
#print(payleyGraph().edges())
#print(nx.is_strongly_regular(payleyGraph()))