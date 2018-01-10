import networkx as nx
#cliquer algorithm is based on the algorithm used in cliquer obtained from https://users.aalto.fi/~pat/cliquer.html
#which is licened under GNU General Public License. Created by Sampo Niskanen and Patric R. J. Ostergard
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

def cliquer(graph):
	vertices=list(graph.nodes(data=False))
	
	#order vertices todo
	orderedVertices=vertices
	#print(vertices)
	subsetOfVertices=[]
	c=[]
	cliques=[]
	for i in range(len(orderedVertices)):
		subsetOfVertices.append(orderedVertices[i])
		#print(subsetOfVertices)
		vertex=orderedVertices[i]
		#print(vertex)
		neighbors=graph.neighbors(vertex)
		#print(neighbors)
		usableVertices=[]
		
		for j in neighbors:
			if j in subsetOfVertices:
				usableVertices.append(j)
		print(usableVertices)
		
		if usableVertices==[]:
			c.append(1)
			cliques.append([vertex])
		elif len(usableVertices)+1<=c[-1]:
			c.append(c[-1])
			cliques.append(cliques[-1])
			print("preprune")
		else:
			candidateClique=[vertex]
			clique=cliquerBranching(c,cliques,graph,usableVertices, candidateClique, orderedVertices)
			c.append(clique[0])
			cliques.append(clique[1])
			print(c)
			print(clique[1])
		print()
		
	return cliques[-1]

def cliquerBranching(c,cliques,graph,usableVertices,candidateClique, orderedVertices):
	if usableVertices==[]:
		#print(candidateClique)
		return (len(candidateClique),candidateClique)
	else:
		for i in usableVertices:
			index=orderedVertices.index(i)
			if((len(candidateClique)+c[index])>c[-1]):
				reducedVertices=[]
				#remove i and things that are not its neighbors from the usable vertices
				neighbors=graph.neighbors(i)
				for j in neighbors:
					if j in usableVertices:
						reducedVertices.append(j)
				#remember we are adding i to our clique hence the +1
				if((len(candidateClique)+len(reducedVertices)+1)>c[-1]):
					cliqueSize=cliquerBranching(c,cliques,graph,reducedVertices,candidateClique+[i], orderedVertices)
					if cliqueSize[0]==c[-1]+1:
						#print("max clique increased")
						return (c[-1]+1,cliqueSize[1])
				#else:
					#print("neighbors prune")
			#else:
				#print("prune")
		return (c[-1],cliques[-1])

cycle=cycleGenerator(5)
powerGraph=graphStrongProdPower(cycle,2)
print(cliquer(nx.complement(powerGraph)))
#print(cliquer(powerGraph))