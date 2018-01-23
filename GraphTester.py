import networkx as nx

from greedyIndepAlg import greedyAlg
from vertexCoverIndep import vertexCoverApprox
from maximumCliqueApprox import cliqueMaxApprox
from partialNeighborhoodSearch import search
from networkx.algorithms import approximation

import graphGenerator
import sys

def loadGraphFromFile(filename):
	with open(filename) as f:
		fileData = f.read()
	f.close()
	
	fileLines=fileData.split("\n")
	
	matrix=[]
	for i in fileLines:
		matrix.append(i.split(","))
		
	for row in matrix:
		for col in range(len(row)):
			row[col]=int(row[col])
	
	""""for i in matrix:
		print(i)"""
	return matrix
	
	
def getGraphBounds(graph, p , k):
	#graphProdMatrix = graphProduct.graphProductPower(graph,power)
	#indepSetLPResult = indepSetLP.indepSetLP(graphProdMatrix)
	greedyAlgResult=greedyAlg(graph.copy())
	print("Greedy Alg result:")
	print(greedyAlgResult)
	print(len(greedyAlgResult))
	print()
	
	#print(graphProdMatrix)
	vertexCoverIndepResult = vertexCoverApprox(graph.copy())
	print("vertex cover result:")
	print(vertexCoverIndepResult)
	print(len(graph.nodes())-len(vertexCoverIndepResult))
	print()
	
	cliqueApproxResult=cliqueMaxApprox(nx.complement(graph),0.01)
	print("Clique approximation result:")
	print(cliqueApproxResult)
	print(len(cliqueApproxResult))
	print()
	#vertices=[]
	#for i in range(len(graphProdMatrix)):
	#	vertices.append(i)
	
	#quantityCliqueResult = cliqueGenerator.quantityCliquesLP(vertices, graphProdMatrix, 10)
	#print("Quantity result:")
	#print(quantityCliqueResult)
	
	#qualityCliqueResult = cliqueGenerator.qualityCliquesLP(vertices, graphProdMatrix, 0.01)
	#print("Quality result:")
	#print(qualityCliqueResult)
	networkxIndep=approximation.maximum_independent_set(graph)
	print("networkx result:")
	print(networkxIndep)
	print(len(networkxIndep))
	print()
	
	b=3
	stocashticResult= search(graph, b ,p, k)
	print("Stocashtic result:")
	print(stocashticResult)
	print(len(stocashticResult))
	print()
	
def rangeTesting(start, finish, graph):
	for i in range(start, finish+1):
		print("Test for power: "+str(i))
		getGraphBounds(graph, i)
		print("Test for power: "+str(i)+" finished.\n")

def main():
	#fileName = sys.argv[1]
	#start = int(sys.argv[2])
	#finish = int(sys.argv[3])
	
	#graph=loadGraphFromFile(fileName)
	
	#rangeTesting(start, finish, graph)
	graph=graphGenerator.cycleGenerator(7)
	graph=nx.strong_product(graph,graph)
	getGraphBounds(graph, 7, 2)
	
	
main()
""""testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
rangeTesting(1,2,testMatrix)

loadGraphFromFile("test.txt")"""