import random
import graphGenerator
from datetime import datetime
from math import log
from math import ceil
import networkx as nx
from itertools import combinations

"""This function gets all the combinations of vertices from a list of vertices of size amount"""
def combos(vertices, amount):
	combos=[]
	for i in combinations(vertices,amount):
		combos.append(list(i))
	return combos

"""Checks if a candidate clique is a clique"""
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

"""Gets the vertices in subVertices which are connect to vertices"""	
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

"""Runs one phase for the algorithm"""	
def phase(subVertices, graph, clique, k, t):
	#if the length of sub vertices is too small then the phase should terminate, we use len(clique)<0 most of the time to stop this occuring
	if((len(subVertices)<int(6*k*t)) and (len(clique)<0)):
		return "clique", clique
	else:
		#we get the partition size
		partitionSize=(2*k*t)
		noOfPartitions=ceil(len(subVertices)/partitionSize)
		partitions=[]
		count=0
		
		#we partition the subgraph vertices into paritions 
		while(count<noOfPartitions):
			tempPart=[]
			i=0
			while((i<int(partitionSize)) and ((count*int(partitionSize)+i)<len(subVertices))):
				tempPart.append(subVertices[count*int(partitionSize)+i])
				i+=1
			count+=1
			partitions.append(tempPart)
		
		#for each parition we get the subsets of size t and check if it is a clique, if it is we get the vertices in the subgraph that are
		#connected to all the vertices in the parition
		for i in partitions:
			if(len(i)<=t):
				bipartite=bipartiteSubgraph(subVertices, i, graph)
				#if the clique and new subgraph are large enough we return them
				if(checkClique(graph, i)) and (len(bipartite)>(len(subVertices)/(2*k-t))):
					#returns the clique and the the new subgraph
					return clique+i, bipartite
			
			else:
				#gets all combinations of vertices in the partition of size t
				combins=combos(i, round(t))
				for j in combins:
					bipartite = bipartiteSubgraph(subVertices, j, graph)
					#print(bipartite)
					if(checkClique(graph, j) and (len(bipartite)>(len(subVertices)/(2*k-t)))):
						return clique+j, bipartite
		#else we say that the subgraph is poor and return it
		return "poor"
	
"""Removes the vertices in vertices from subVertices"""
def removeVertices(vertices, subVertices):
	for i in subVertices:
		vertices.remove(i)

"""Returns all the vertices in vertices and not in clique"""
def newSubVertices(vertices, clique):
	subVertices=[]
	for i in vertices:
		if not (i in clique):
			subVertices.append(i)
	return subVertices

"""Runs the clique approximation algorithm"""	
def cliqueApprox(graph, k, t):
	#if the graph is too small than we output a clique of size 1
	if(len(graph.nodes())<2*k*t):
		return [graph.nodes[0]]
	
	#else we run each phase until subVertices is emapty
	clique=[]
	subVertices = list(graph.nodes())
	while len(subVertices)>0:
		#gets the results of the phase
		temp=phase(subVertices, graph, clique, k, t)
		#if it is poor we return a clique of size 1
		if temp =="poor":
			if(subVertices !=[]):
				clique.append(subVertices[0])
				return clique
			else:
				return clique
		
		#else if the phase returned a clique then we return it
		elif temp[0]=="clique":
			clique=temp[1]
			if(subVertices!=[]):
				return clique.append(subVertices[0])
			else:
				return clique
		
		#else we go onto the next phase with a new candidate clique and set of sub vertice
		else:
			clique=temp[0]
			subVertices=temp[1]
	return clique

"""The Clique approximation algorithm"""
def cliqueMaxApprox(graph,b):
	#creates the constants need for the algorithm and runs it
	n=len(graph.nodes())
	t=log(n)/log(log(n))	
	k = log(n)**b
	
	#returns the results
	return cliqueApprox(graph, k ,t)