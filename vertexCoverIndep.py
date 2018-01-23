import networkx as nx
import random
from datetime import datetime

def starCycleGen(n,m):
	graph=nx.Graph()
	vertex=0
	for i in range(m):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
		vertex+=1
	
	print(graph.edges())
	for i in range(m):
		for j in range(n):
			graph.add_edge(vertex,i)
			graph.add_edge(i,vertex)
			vertex+=1
	return graph
	
def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph
	
def vertexCoverApprox(graph):
	vertexCover=[]
	random.seed(datetime.now())
	
	while(len(graph.edges())>0):
		edges=list(graph.edges())
		randomEdge=random.randint(0,len(edges)-1)
		edge=edges[randomEdge]
		
		vertexCover.append(edge[0])
		vertexCover.append(edge[1])
		
		graph.remove_node(edge[0])
		graph.remove_node(edge[1])
	
	return vertexCover


#print(vertexCoverApprox(starCycleGen(4,5)))