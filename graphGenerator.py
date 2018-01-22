import networkx as nx

import random
from datetime import datetime

def probabilisticGraph 
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
	
print(starCycleGen(4,3).edges())