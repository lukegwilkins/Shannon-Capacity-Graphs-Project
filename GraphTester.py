import networkx as nx

from greedyIndepAlg import greedyAlg
from vertexCoverIndep import vertexCoverApprox
from maximumCliqueApprox import cliqueMaxApprox
from partialNeighborhoodSearch import search
from networkx.algorithms import approximation

import graphGenerator
import sys
	
"""Function runs each of the approximation algorithms on the graph and outputs them to a file"""
def getGraphBounds(graph, p , k, filename):
	#creates the file to store the results
	filename="results\\"+filename+".csv"
	file=open(filename,'w')
	
	#runs the greedy algorithm and outputs the results
	greedyAlgResult=greedyAlg(graph.copy())
	print("Greedy Alg result:")
	print(greedyAlgResult)
	print(len(greedyAlgResult))
	print()
	file.write(str(len(greedyAlgResult))+"\n")
	
	#run the vertex cover approximation algorithm 50 times and outputs the best result
	vertexCoverIndepResult = vertexCoverApprox(graph.copy())
	for i in range(50):
		temp = vertexCoverApprox(graph.copy())
		if(len(temp)<len(vertexCoverIndepResult)):
			vertexCoverIndepResult=temp
	print("vertex cover result:")
	print(len(graph.nodes())-len(vertexCoverIndepResult))
	print()
	file.write(str(len(graph.nodes())-len(vertexCoverIndepResult))+"\n")
	
	#runs the algorithm for approximating clique and outputs its results
	cliqueApproxResult=cliqueMaxApprox(nx.complement(graph),0.01)
	print("Clique approximation result:")
	print(cliqueApproxResult)
	print(len(cliqueApproxResult))
	print()
	file.write(str(len(cliqueApproxResult))+"\n")
	
	#if the graph isn't too large we run the algorithm for networkx and outputs its results
	if(len(graph.nodes())<2200):
		networkxIndep=approximation.maximum_independent_set(graph)
		print("networkx result:")
		print(networkxIndep)
		print(len(networkxIndep))
		print()
		file.write(str(len(networkxIndep))+"\n")
	else:
		print("Too big for networkx")
	
	#if the graph isn't too large for the stochastic algorithm then we run it and output its results
	if(len(graph.nodes())<400):
		b=2
		stochasticResult= search(graph, b ,p, k)
		print("Stochastic result:")
		print(stochasticResult)
		print(len(stochasticResult))
		print()
		file.write(str(len(stochasticResult)))
		file.write("\n")
		file.write(str(stochasticResult))
	else:
		print("Graph too big for stochastic")

"""Main method"""
def main():
	#we get the size of the graph and the power we are going to test up to
	n = int(sys.argv[2])
	k = int(sys.argv[3])
	#we create the base graph
	graph=graphGenerator.regularGraph(n,8)
	for i in range(1,k+1):
		#we get the file name for the graph
		filename = sys.argv[1]+"_to_"+str(i)
		
		#we create the graph's strong product power and get the independent set sizes for it
		if(i>1):
			graphPrime=graphGenerator.graphStrongProdPower(graph,i)
			getGraphBounds(graphPrime, n, k, filename)
		else:
			getGraphBounds(graph, n, k, filename)
	
	
main()
""""testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
rangeTesting(1,2,testMatrix)

loadGraphFromFile("test.txt")"""