from copy import copy
import numpy as np
from scipy.optimize import linprog
from itertools import combinations as iterCombos
from GraphScripts.maximumClique import cliqueMaxApprox
			
def checkClique(edges, clique):
	validClique=True
	
	i=0
	while(i<len(clique) and validClique):
		j=i+1
		while(j<len(clique) and validClique):
			if(edges[clique[i]][clique[j]]==0):
				validClique=False
			j+=1
		i+=1
	return validClique
			
def generateFixedSizeCliques(vertices,edges, size):
	cliques=[]
	amount = 6000
	for i in iterCombos(vertices,size):
		if checkClique(edges, i):
			cliques.append(list(i))
			if len(cliques)>amount:
				break
	return cliques

def generateCliques(vertices, edges, amount):	
	cliques=[]
	for i in range(3,amount+1):
		cliques= cliques+generateFixedSizeCliques(vertices,edges,i)
	return addEdges(edges, vertices, cliques)

def listIsSubList(listA, listB):
	for i in listA:
		if i not in listB:
			return False
	return True
	
def isSubListOfElement(listA, listOfLists):
	for i in listOfLists:
		if listIsSubList(listA,i):
			return True
	return False
	
def cliqueQualityGen(graph, vertices, startingClique):
	n=len(vertices)
	#count=3
	amount=len(startingClique)-1
	temp=copy(vertices)
	cliques=[startingClique]
	for i in range(amount, 2,-1):
		for j in iterCombos(vertices,i):
			if checkClique(graph,list(j)):
				if not(isSubListOfElement(j,cliques)):
					cliques.append(list(j))
					break
	
	return addEdges(graph, vertices, cliques)

def addEdges(graph, vertices, cliques):
	for i in vertices:
		#cliques.append([i])
		for j in vertices:
			if(graph[i][j]==1 and i<j and i!=j):
				cliques.append([i,j])
	return cliques
	
def createAndRunLP(cliques,vertices):
	noOfRows=len(cliques)#-len(vertices)
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
	#print(res["fun"])
	return -res["fun"]
	
def qualityCliquesLP(vertices, edges, b):
	#print("quality")
	maxClique=cliqueMaxApprox(vertices, edges,b)
	print(maxClique)
	cliques=cliqueQualityGen(edges, vertices, maxClique)
	#print(cliques)
	result=createAndRunLP(cliques, vertices)
	return result

def quantityCliquesLP(vertices, edges, amount):
	#print("quantity")
	cliques=generateCliques(vertices, edges, amount)
	#print(cliques)
	result=createAndRunLP(cliques, vertices)
	return result
#matrix=[[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0], [0,0,1,1,1],[1,0,0,1,1]]
""""matrix=np.ones((25,25))
#matrix = np.ones((5,5))
vertices=[0,1,2,3,4,5,6,7,8,9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24]
quantityCliquesLP(vertices, matrix, 4)
#cliques=cliqueQualityGen(matrix,[0,1,2,3,4,5,6,7,8,9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24],14)
print(qualityCliquesLP([0,1,2,3,4,5,6,7,8,9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24],matrix, 0.01))
#print(createLP(cliques, [0,1,2,3,4]))"""
