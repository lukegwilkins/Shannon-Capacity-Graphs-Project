import random
import networkx as nx
#from networkx.algorithms import approximation
from cliquerAlg import cliquer
from datetime import datetime
random.seed(datetime.now())

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
	#print(binaryOfK)
	for i in range(len(binaryOfK)-1,-1,-1):
		if(binaryOfK[i]=='1'):
			if(resultingGraph=="empty"):
				resultingGraph=currentProdGraph
			else:
				resultingGraph=nx.strong_product(graph,currentProdGraph)
		
		if(i>0):
			currentProdGraph=nx.strong_product(currentProdGraph,currentProdGraph)
	return resultingGraph

def nodeConversion(node):
	if type(node) is int:
		return [node]
	else:
		#print(node)
		left = node[0]
		right = node[1]
		node=nodeConversion(left)+nodeConversion(right)
		return node

def leeDistance(vOne,vTwo,p):
	distance=0	
	if(type(vOne) is int):
		difference = abs(vOne-vTwo)
		if(difference<(p-difference)):
			distance+=difference
		else:
			distance +=p-difference
	else:
		vOneConv=nodeConversion(vOne)
		vTwoConv=nodeConversion(vTwo)
		for i in range(len(vOne)):
			difference = abs(vOneConv[i]-vTwoConv[i])
			if(difference<(p-difference)):
				distance+=difference
			else:
				distance +=p-difference
	return distance

def distanceVertices(indepSet, vertex, b, p):
	returnList=[]
	for i in indepSet:
		if(leeDistance(i,vertex, p)>b):
			returnList.append(i)
	return returnList


def graphWithNeighborsRemoved(graph, vertices):
	returnGraph = graph.copy()
	for i in vertices:
		neighbors =[]
		for j in returnGraph.neighbors(i):
			neighbors.append(j)
		#print(neighbors)
		for j in neighbors:
			returnGraph.remove_node(j)
		
		returnGraph.remove_node(i)
	return returnGraph

def unionList(listA, listB):
	for i in listB:
		if i not in listA:
			listA.append(i)
	return listA
	
def search(graph, b, p, k):
	indepSet=greedyAlg(graph.copy())
	indepSetBest=indepSet
	condition=True
	count=0
	#print("boop")
	while condition:
		i = indepSet[random.randint(0,len(indepSet)-1)]
		indepSetLoop=distanceVertices(indepSet, i, b, p)
		subGraph=graphWithNeighborsRemoved(graph,indepSetLoop)
		subGraph.remove_node(i)
		#print(subGraph.nodes())
		#print("hello")
		print(len(subGraph.nodes()))
		maxInd=cliquer(nx.complement(subGraph))
		#print(maxInd)
		#print(indepSetLoop)
		indepSet= unionList(indepSetLoop,maxInd)
		#print(indepSet)
		if(len(indepSet)>len(indepSetBest)):
			indepSetBest=indepSet
		count+=1
		print(count)
		#print()
		iters=100
		if(count>iters):
			condition=False
	#filename="results/c"+str(p)+"b"+str(b)+"k"+str(k)+"Iter"+str(iters)+".txt"
	#file=open(filename,'w')
	#file.write(str(indepSetBest))
	return indepSetBest

def minimumDegreeNode(graph):
	nodes=graph.nodes()
	degrees=graph.degree(nodes)
	minimumNode=(-1,-1)
	for node in degrees:
		if (node[1]<minimumNode[1]) or (minimumNode[0]==-1):
			minimumNode=node
		
	return minimumNode[0]
	
def greedyAlg(graph):
	#print(graph.nodes())
	indepSet=[]
	while len(graph.nodes())!=0:
		#print(graph.nodes())
		minimumNode=minimumDegreeNode(graph)
		indepSet.append(minimumNode)
		#print(minimumNode)
		neighbors=[]
		for i in graph.neighbors(minimumNode):
			neighbors.append(i)
		
		for i in neighbors:
			graph.remove_node(i)
		graph.remove_node(minimumNode)
		#print(len(graph.nodes()))
	return indepSet

""""k=3
p=9
graph=graphStrongProdPower(cycleGenerator(p),k)
#indepSet=greedyAlg(graph.copy())
#print(indepSet)
#print(len(indepSet))
#print(len(indepSet)**(1/k))

#print(graph.nodes())
tuple=(5,((1,2),(3,4)))
print(nodeConversion(tuple))

print(leeDistance(((1,2),1), ((2,4),6),7))
vertices=distanceVertices(indepSet, (1,2),3,7)
vertices
print(vertices)
print(graph.nodes())
reducedGraph=graphWithNeighborsRemoved(graph, vertices)
reducedGraph.remove_node((1,2))
print(reducedGraph.nodes())

print(unionList([2,3,6,1],[3,2,4,7,10,9]))
indep=search(graph,3, p, k)
print(indep)
print(len(indep))"""
