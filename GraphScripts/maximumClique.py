import random
from datetime import datetime
from math import log
from math import ceil
import numpy as np
from copy import copy
from itertools import combinations


#print(t)
def combos(vertices, amount):	
	combos=[]
	for i in combinations(vertices,amount):
		combos.append(list(i))
	return combos
	
def checkClique(graph, clique):
	validClique=True
	#print(graph)
	i=0
	while(i<len(clique) and validClique):
		j=i+1
		while(j<len(clique) and validClique):
			if(graph[clique[i]][clique[j]]==0):
				validClique=False
			j+=1
		i+=1
	return validClique
	
def bipartiteSubgraph(graph,subVertices, edges):
	bipartite=[]
	for i in graph:
		if i not in subVertices:
			connected=True
			for j in subVertices:
				if(edges[i][j]==0):
					connected=False
			if(connected):
				bipartite.append(i)
	return bipartite

def phase(subGraph, edges, clique, k ,t):
	if((len(subGraph)<int(6*k*t)) and (len(clique)<0)):
		return "clique",clique
	else:
		partitionSize=(2*k*t)
		noOfPartitions=ceil(len(subGraph)/partitionSize)
		partitions=[]
		count=0
		#print(partitionSize)
		while(count<noOfPartitions):
			tempPart=[]
			i=0
			while((i<int(partitionSize)) and ((count*int(partitionSize)+i)<len(subGraph))):
				tempPart.append(subGraph[count*int(partitionSize)+i])
				i+=1
			count+=1
			partitions.append(tempPart)
		#print(partitions)
		for i in partitions:
			if(len(i)<=t):
				bipartite=bipartiteSubgraph(subGraph,i,edges)
				if(checkClique(edges,i) and (len(bipartite)>(len(subGraph)/(2*k-t)))):
					return clique+i, bipartite
			else:
				combins=combos(i,round(t))
				#print(combins)
				for j in combins:
					bipartite=bipartiteSubgraph(subGraph,j,edges)
					
					if(checkClique(edges, j) and (len(bipartite)>(len(subGraph)/(2*k-t)))):
						return clique+j, bipartite
		return "poor"

def removeVertices(vertices, subVertices):
	for i in subVertices:
		vertices.remove(i)

def newSubVertices(vertices,clique):
	subVertices=[]
	for i in vertices:
		if not (i in clique):
			subVertices.append(i)
	return subVertices

def cliqueApprox(vertices,edges,k,t):
	if(len(vertices)<2*k*t):
		return [vertices[0]]
	clique=[]
	subVertices=vertices
	while subVertices != []:
		#print("clique is "+str(clique))
		temp=phase(subVertices,edges,clique,k,t)
		if temp =="poor":
			#print("poor")
			#print(subVertices)
			removeVertices(vertices,subVertices)
			subVertices= newSubVertices(vertices, clique)
			#print(vertices)
			#print("poor")
			#print(clique)
			#print(subVertices)
			if(subVertices!=[]):
				return clique.append(subVertices[0])
			else:
				return clique
			
		elif temp[0]=="clique":
			#print("clique")
			#print(temp[1])
			clique=temp[1]
			if(subVertices!=[]):
				return clique.append(subVertices[0])
			else:
				return clique
		else:
			#print("next phase")
			clique= temp[0]
			subVertices=temp[1]
			#print(clique, subVertices)
	#print(clique)
	return clique

def cliqueMaxApprox(vertices,edges,b):
	n=len(vertices)
	t=log(n)/log(log(n))
	
	k = log(n)**b
	
	return cliqueApprox(vertices, edges, k,t)


""""completeGraph=np.ones((30,30))
random.seed(datetime.now())
for i in range(len(completeGraph)):
	for j in range(i+1,len(completeGraph)):
		if(random.random()<0.2):
			completeGraph[i][j]=0
			completeGraph[j][i]=0
			
for i in completeGraph:
	print(i)
		
#print(bipartiteSubgraph([0,1,2,3,4],[1,2],completeGraph))

#print(phase([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],completeGraph,[],2,2))
clique=cliqueMaxApprox([0,1,2,3,4,5,6,7,8,9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],completeGraph, 0.01)
print(clique)
print(checkClique(completeGraph, clique))"""