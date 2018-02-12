import networkx as nx
import numpy as np
from scipy.optimize import linprog
from greedyIndepAlg import greedyAlg
import graphGenerator

lpIsMinimizer=True
def fractionalIndep(graph):
	n=len(graph.nodes())
	cliques=list(nx.find_cliques(graph))
	m=len(cliques)
	
	matrixA=np.zeros((m,n))
	
	matrixLine=0
	for clique in cliques:
		for j in clique:
			matrixA[matrixLine][j]=1
		matrixLine+=1
	constraintUpperBounds = np.ones(m)
	
	if lpIsMinimizer: 
		objFunction = -1*np.ones(n)
	else:
		objFunction = np.ones(n)
		
	variableBounds=(0,1)
	res = linprog(objFunction, A_ub=matrixA, b_ub= constraintUpperBounds, bounds=variableBounds)
	
	return -res["fun"]
	

graph = graphGenerator.paleyGraph()
print(fractionalIndep(graph))
print(greedyAlg(graph))