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
	
	
def getGraphBounds(graph, p , k, filename):
	#graphProdMatrix = graphProduct.graphProductPower(graph,power)
	#indepSetLPResult = indepSetLP.indepSetLP(graphProdMatrix)
	filename="results\\"+filename+".csv"
	file=open(filename,'w')
	
	greedyAlgResult=greedyAlg(graph.copy())
	print("Greedy Alg result:")
	print(greedyAlgResult)
	print(len(greedyAlgResult))
	print()
	file.write(str(len(greedyAlgResult))+"\n")
	
	#print(graphProdMatrix)
	vertexCoverIndepResult = vertexCoverApprox(graph.copy())
	for i in range(50):
		temp = vertexCoverApprox(graph.copy())
		if(len(temp)<len(vertexCoverIndepResult)):
			vertexCoverIndepResult=temp
	print("vertex cover result:")
	#print(vertexCoverIndepResult)
	print(len(graph.nodes())-len(vertexCoverIndepResult))
	print()
	file.write(str(len(graph.nodes())-len(vertexCoverIndepResult))+"\n")
	
	cliqueApproxResult=cliqueMaxApprox(nx.complement(graph),0.01)
	print("Clique approximation result:")
	print(cliqueApproxResult)
	print(len(cliqueApproxResult))
	print()
	file.write(str(len(cliqueApproxResult))+"\n")
	
	#vertices=[]
	#for i in range(len(graphProdMatrix)):
	#	vertices.append(i)
	
	#quantityCliqueResult = cliqueGenerator.quantityCliquesLP(vertices, graphProdMatrix, 10)
	#print("Quantity result:")
	#print(quantityCliqueResult)
	
	#qualityCliqueResult = cliqueGenerator.qualityCliquesLP(vertices, graphProdMatrix, 0.01)
	#print("Quality result:")
	#print(qualityCliqueResult)
	if(len(graph.nodes())<2200):
		networkxIndep=approximation.maximum_independent_set(graph)
		print("networkx result:")
		print(networkxIndep)
		print(len(networkxIndep))
		print()
		file.write(str(len(networkxIndep))+"\n")
	else:
		print("Too big for networkx")
	
	if(len(graph.nodes())<400):
		b=2
		stochasticResult= search(graph, b ,p, k)
		print("Stochastic result:")
		print(stochasticResult)
		print(len(stochasticResult))
		print()
		file.write(str(len(stochasticResult)))
	else:
		print("Graph too big for stochastic")
	
def rangeTesting(start, finish, graph):
	for i in range(start, finish+1):
		print("Test for power: "+str(i))
		getGraphBounds(graph, i)
		print("Test for power: "+str(i)+" finished.\n")

def main():
	#filename = sys.argv[1]
	n = int(sys.argv[2])
	#d = int(sys.argv[3])
	k = int(sys.argv[3])
	#start = int(sys.argv[2])
	#finish = int(sys.argv[3])
	graph=graphGenerator.paleyGraph()
	#graph=graphGenerator.cograph(n)
	#print(graph.edges())
	for i in range(1,k+1):
		#"_size_"+sys.argv[2]+"_degree_"+sys.argv[3]+
		filename = sys.argv[1]+"_to_"+str(i)
		#graph=loadGraphFromFile(fileName)
		
		#rangeTesting(start, finish, graph)
		#n=7
		#graph=graphGenerator.starCycleGen(6,1)
		
		if(i>1):
			graphPrime=graphGenerator.graphStrongProdPower(graph,i)
			getGraphBounds(graphPrime, n, k, filename)
		else:
			getGraphBounds(graph, n, k, filename)
	
	
main()
""""testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
rangeTesting(1,2,testMatrix)

loadGraphFromFile("test.txt")"""