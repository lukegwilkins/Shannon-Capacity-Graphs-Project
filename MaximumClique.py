from GraphScripts import graphProduct
from math import log
from math import ceil
import numpy as np
from copy import copy
testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
graphProdMatrix = graphProduct.graphProductPower(testMatrix,2)
n=len(testMatrix)
t=log(n)/log(log(n))
k=4
subVertices=[]

#print(t)
def combinations(vertices, amount):
	n=len(vertices)
	temp=copy(vertices)
	p=[]
	for i in range(1,2**n):
		x=bin(i)[2:].zfill(n)
		if(x.count('1')==amount):
			m=[]
			for j in range(n):
				if x[j]=='1':
					m.append(temp[j])
			p.append(m)
	return p
	
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
	
def bipartiteSubgraph(graph,vertices, edges):
	bipartite=[]
	for i in graph:
		if(i not in vertices):
			connected=True
			for j in vertices:
				if(edges[i][j]==0):
					connected=False
			if(connected):
				bipartite.append(i)
	return bipartite

def phase(graph, subGraph, edges, clique, k ,t):
	if((len(subGraph)<6*k*t) and (len(clique)>0)):
		return "clique",clique
	else:
		partitionSize=(2*k*t)
		
		noOfPartitions=ceil(len(subGraph)/partitionSize)
		partitions=[]
		count=0
		while(count<noOfPartitions):
			tempPart=[]
			i=0
			while((i<partitionSize) and ((count*int(partitionSize)+i)<len(subGraph))):
				tempPart.append(subGraph[count*int(partitionSize)+i])
				i+=1
			count+=1
			partitions.append(tempPart)
		
		for i in partitions:
			if(len(i)<=t):
				bipartite=bipartiteSubgraph(subGraph,i,edges)
				if(checkClique(edges,i) and (len(bipartite)>(len(subGraph)/(2*k-t)))):
					return i, bipartite
			else:
				combos=combinations(i,int(t))
				for j in combos:
					bipartite=bipartiteSubgraph(subGraph,j,edges)					
					if(checkClique(edges, j) and (len(bipartite)>(len(subGraph)/(2*k-t)))):
						return clique+j, bipartite
		return "poor"

def removeVertices(vertices, subVertices):
	for i in subVertices:
		vertices.remove(i)

def newSubVertices(graph,clique):
	subVertices=[]
	for i in graph:
		if !(i in clique):
			subVertices.append(i)
	return subVertices

def cliqueApprox(graph,edges,k,t):
	clique=[]
	subVertices=graph
	while True:
		temp=phase(graph,subVertices,edges,clique,k,t)
		if temp =="poor":
			print("poor")
			print(subVertices)
			removeVertices(graph,subVertices)
			subVertices= newSubVertices(graph, clique)
			print(graph)
		elif temp[0]=="clique":
			print("clique")
			print(temp[1])
			return temp[1]
		else:
			print("next phase")
			clique= temp[0]
			subVertices=temp[1]
			print(clique, subVertices)
		
completeGraph=np.ones((30,30))

#print(bipartiteSubgraph([0,1,2,3,4],[1,2],completeGraph))

#print(phase([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],completeGraph,[],2,2))
print(cliqueApprox([0,1,2,3,4,5,6,7,8,9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],completeGraph,2,2))
