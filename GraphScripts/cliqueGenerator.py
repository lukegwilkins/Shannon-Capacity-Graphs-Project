from copy import copy
import numpy as np
from scipy.optimize import linprog
""""def incrementClique(graph,clique):
	vertex=clique[0]
	cliques = []
	#cliques.append(clique)
	for i in range(len(graph[vertex])):
		if i not in clique:
			newVertex=True
			j=0
			while j<len(clique) and newVertex:
				if graph[i][clique[j]]==0:
					newVertex=False
				j+=1
			if newVertex:
				newClique=copy(clique)
				newClique.append(i)
				cliques.append(newClique)
	return cliques


def combination(vertices, amount):
	cliqueMatrix=[]
	tempVertices=copy(vertices)
	for i in vertices:
		for j in range(amount):
"""
			
def checkClique(graph, clique):
	validClique=True
	
	i=0
	while(i<len(clique) and validClique):
		j=i+1
		while(j<len(clique) and validClique):
			if(graph[clique[i]][clique[j]]==0):
				validClique=False
			j+=1
		i+=1
	return validClique
			
def combinations(vertices, amount):
	n=len(vertices)
	temp=copy(vertices)
	p=[]
	for i in range(1,2**n):
		x=bin(i)[2:].zfill(n)
		if(x.count('1')<=amount):
			m=[]
			for j in range(n):
				if x[j]=='1':
					m.append(temp[j])
			p.append(m)
	return p

def generateCliques(graph,amount):
	vertices=[]
	for i in range(len(graph)):
		vertices.append(i)
	
	combos=combinations(vertices, amount)
	i=0
	while i<len(combos):
		if checkClique(graph, combos[i]):
			i+=1
		else:
			del combos[i]
	return combos

def createLP(cliques,vertices):
	noOfRows=len(cliques)-len(vertices)
	matrixA = np.zeros((noOfRows,len(vertices)))
	
	matrixLine=0
	for i in range(len(cliques)):
		if(len(cliques[i])>1):
			for j in range(len(cliques[i])):
				matrixA[matrixLine][cliques[i][j]]=1
			matrixLine+=1
	constraintUpperBounds = np.ones(noOfRows)
	
	objFunction=-1*np.ones(len(vertices))
	
	res = linprog(objFunction, A_ub=matrixA, b_ub= constraintUpperBounds)
	print(res)
	return -res["fun"]
	
	
matrix=[[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0], [0,0,1,1,1],[1,0,0,1,1]]

""""combo=combinations([0,1,2,3,4],3)
print(combo)
print(len(combo))

print(checkClique(matrix, [0,1]))"""

cliques=generateCliques(matrix,2)
print(cliques)
print(createLP(cliques, [0,1,2,3,4]))
