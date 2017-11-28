import networkx as nx
from networkx.algorithms import approximation
from GraphScripts import vertexCoverIndep
def cycleGenerator(n):
	graph=nx.Graph()
	for i in range(n):
		graph.add_edge(i,(i+1)%n)
		graph.add_edge((i-1)%n,i)
	return graph

def graphStrongProdPower(graph,k):
	binaryOfK=bin(k)[2:]
	resultingGraph="empty"
	currentProdGraph=graph
	print(binaryOfK)
	for i in range(len(binaryOfK)-1,-1,-1):
		if(binaryOfK[i]=='1'):
			if(resultingGraph=="empty"):
				resultingGraph=currentProdGraph
			else:
				resultingGraph=nx.strong_product(graph,currentProdGraph)
		
		if(i>0):
			currentProdGraph=nx.strong_product(currentProdGraph,currentProdGraph)
	return resultingGraph

def simpleStrongProd(graph,k):
	currentGraph=graph
	for i in range(k-1):
		currentGraph=nx.strong_product(currentGraph,graph)
		print(i)
	return currentGraph
	
def cyclePowerTesters(n,startK,endK):
	graph=cycleGenerator(n)
	startingGraph=graphStrongProdPower(graph,startK)
	print("cycle is size "+str(n))
	vertexCoverIndep.vertexCoverApprox(startingGraph)
	for i in range(startK,endK+1):
		#print(startingGraph.nodes())
		indep=approximation.maximum_independent_set(startingGraph)
		print("power is "+str(i))
		#print(indep)
		print("indep size is "+str(len(indep)))
		print("Shannon capacity is "+str(len(indep)**(1/i)))
		print()
		startingGraph=nx.strong_product(startingGraph,graph)
		
		

""""graph=cycleGenerator(5)
prodGraph=graphStrongProdPower(graph,3)
indep=approximation.maximum_independent_set(prodGraph)
print(indep)
print(len(indep))"""
#graph = cycleGenerator(7)
#print("graph made")
#pGraph=simpleStrongProd(graph,4)
#print(pGraph.nodes())
#print(len(pGraph))
cyclePowerTesters(7,2,2)
#print(len(prodGraph.nodes()))
#print(prodGraph.edges())