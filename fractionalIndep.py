import networkx as nx
import numpy as np
from scipy.optimize import linprog
from greedyIndepAlg import greedyAlg
import graphGenerator

#stores whether the LP package we are using is minimizer or maximizer
lpIsMinimizer=True

"""Function that figures out the size of the fractional independent set for the graph"""
def fractionalIndep(graph):
	n=len(graph.nodes())
	#gets all the unique cliques in a graph
	cliques=list(nx.find_cliques(graph))
	m=len(cliques)
	
	#creates the constraint matrix for the LP
	matrixA=np.zeros((m,n))
	
	matrixLine=0
	for clique in cliques:
		for j in clique:
			matrixA[matrixLine][j]=1
		matrixLine+=1
	#gets the upper bounds for the constraints
	constraintUpperBounds = np.ones(m)
	
	#creates the objective function for the LP
	if lpIsMinimizer: 
		objFunction = -1*np.ones(n)
	else:
		objFunction = np.ones(n)
	
	#gets the variable bounds
	variableBounds=(0,1)
	
	#calculates the results for the linear program
	res = linprog(objFunction, A_ub=matrixA, b_ub= constraintUpperBounds, bounds=variableBounds)
	#returns the results
	return -res["fun"]
	

graph = graphGenerator.paleyGraph25()
print(fractionalIndep(graph))
print(greedyAlg(graph))