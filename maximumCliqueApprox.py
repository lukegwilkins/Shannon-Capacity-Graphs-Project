import random
from datetime import datetime
from math import log
from math import ceil
import networkx as nx
from itertools import combinations

def combos(vertices, amount):
	combos=[]
	for i in combinations(vertices,amount):
		combos.append(list(i))
	return combos
	
def checkClique(graph, clique):
	validClique=True
	i=0
	while(i<len(clique) and validClique):
		j=i+1
		while(j<len(clique) and validClique):
			if not graph.has_edge(clique[i],clique[j]):
				validClique=False
			j+=1
		i+=1
	return validClique
	
def bipartiteSubgraph(vertices, subVertices, graph):
	bipartite=[]
	for i in vertices:
		if i not in subVertices:
			connected=True
			for j in subVertices:
				if not graph.has_edge(i,j):
					connected=False
			if(connected):
				bipartite.append(i)
	return bipartite
	
def phase(subVertices, graph, clique, k, t):
	if((len(subVertices)<int(6*k*t)) and (len(clique)<0)):
		return "clique", clique
	else:
		partitionSize=(2*k*t)
		noOfPartitions=ceil(len(subVertices)/partitionSize)
		partitions=[]
		count=0
		
		while(count<noOfPartitions):
			tempPart=[]
			i=0
			while((i<int(partitionSize)) and ((count*int(partitionSize)+i)<len(subVertices))):
				tempPart.append(subVertices[count*int(partitionSize)+i])
				i+=1
			count+=1
			partitions.append(tempPart)
		#print(partitions)
		for i in partitions:
			if(len(i)<=t):
				bipartite=bipartiteSubgraph(subVertices, i, graph)
				if(checkClique(graph, i)) and (len(bipartite)>(len(subVertices)/(2*k-t))):
					return clique+i, bipartite
			
			else:
				combins=combos(i, round(t))
				for j in combins:
					bipartite = bipartiteSubgraph(subVertices, j, graph)
					#print(bipartite)
					if(checkClique(graph, j) and (len(bipartite)>(len(subVertices)/(2*k-t)))):
						return clique+j, bipartite
		return "poor"
def removeVertices(vertices, subVertices):
	for i in subVertices:
		vertices.remove(i)

def newSubVertices(vertices, clique):
	subVertices=[]
	for i in vertices:
		if not (i in clique):
			subVertices.append(i)
	return subVertices
	
def cliqueApprox(graph, k, t):
	if(len(graph.nodes())<2*k*t):
		return [graph.nodes[0]]
	clique=[]
	subVertices = list(graph.nodes())
	#print(subVertices)
	while len(subVertices)>0:
		temp=phase(subVertices, graph, clique, k, t)
		#print(temp)
		#print(clique)
		#print(subVertices)
		if temp =="poor":
			#removeVertices(list(graph.nodes()), subVertices)
			#subVertices=newSubVertices(list(graph.nodes()), clique)
			if(subVertices !=[]):
				#print(subVertices[0])
				#temp=clique
				clique.append(subVertices[0])
				#print(temp)
				return clique
			else:
				return clique
		
		elif temp[0]=="clique":
			clique=temp[1]
			if(subVertices!=[]):
				return clique.append(subVertices[0])
			else:
				return clique
		
		else:
			clique=temp[0]
			subVertices=temp[1]
			#print(subVertices)
			#input()
	return clique
def cliqueMaxApprox(graph,b):
	n=len(graph.nodes())
	t=log(n)/log(log(n))
	
	k = log(n)**b
	
	return cliqueApprox(graph, k ,t)
""""graph = nx.complete_graph(25)
random.seed(datetime.now())
for i in range(25):
	for j in range(i+1, 25):
		if(random.random()<0.2):
			graph.remove_edge(i,j)

#print(graph.edges())
#graph=nx.strong_product(graph,graph)
print(cliqueMaxApprox(graph,0.01))"""