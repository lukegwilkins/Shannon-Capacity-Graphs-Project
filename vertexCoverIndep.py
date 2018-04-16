import networkx as nx
import random
from datetime import datetime

"""Vertex cover approximation algorithm"""	
def vertexCoverApprox(graph):
	vertexCover=[]
	random.seed(datetime.now())
	
	#picks a random edge and adds it 2 end points to the vertex cover
	#it removes endpoints from the graph, it repeats until all edges are removed
	while(len(graph.edges())>0):
		#picks a random edge
		edges=list(graph.edges())
		randomEdge=random.randint(0,len(edges)-1)
		edge=edges[randomEdge]
		print(edge)
		
		#adds it edges to the vertex cover
		vertexCover.append(edge[0])
		vertexCover.append(edge[1])
		
		#removes the endpoints from the graphs
		graph.remove_node(edge[0])
		graph.remove_node(edge[1])
	
	#returns the vertex cover
	return vertexCover


