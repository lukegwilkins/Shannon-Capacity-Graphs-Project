import networkx as nx
from vertexOrdering import graphColouringOrder
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
	#vertices=list(graph.nodes(data=False))
	
	#order vertices todo
	orderedVertices=graphColouringOrder(graph)
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
		#print(usableVertices)
		
		if usableVertices==[]:
			c.append(1)
			cliques.append([vertex])
		elif len(usableVertices)+1<=c[-1]:
			c.append(c[-1])
			cliques.append(cliques[-1])
			#print("preprune")
		else:
			candidateClique=[vertex]
			clique=cliquerBranching(c,cliques,graph,usableVertices, candidateClique, orderedVertices)
			c.append(clique[0])
			cliques.append(clique[1])
			print(c)
			#print(clique[1])
		#print()
		
	return cliques[-1]

def cliquerBranching(c,cliques,graph,usableVertices,candidateClique, orderedVertices):
	if usableVertices==[]:
		#print(candidateClique)
		return (len(candidateClique),candidateClique)
	else:
		i=0
		while i<len(usableVertices):
			vertex=usableVertices[i]
			index=orderedVertices.index(vertex)
			if((len(candidateClique)+c[index])>c[-1]):
				reducedVertices=[]
				#remove i and things that are not its neighbors from the usable vertices
				neighbors=graph.neighbors(vertex)
				for j in neighbors:
					if j in usableVertices:
						reducedVertices.append(j)
				#remember we are adding i to our clique hence the +1
				if((len(candidateClique)+len(reducedVertices)+1)>c[-1]):
					cliqueSize=cliquerBranching(c,cliques,graph,reducedVertices,candidateClique+[vertex], orderedVertices)
					if cliqueSize[0]==c[-1]+1:
						#print("max clique increased")
						return (c[-1]+1,cliqueSize[1])
					#here we check vertex i but it didn't result in a clique of large enough size, since we explore all
					#sub trees with vertex i we can delete it to remove sub trees which are the same but just a reordering
					#of the vertices in the sub tree
					else:
						del usableVertices[i]
				#here we delete i since the size of the neighbours in the usable vertices isn't large enough to result in
				#a bigger clique
				else:
					del usableVertices[i]
			
			#branches not explored only thought not worth using vertex, but a clique for a vertex after it in the ordering
			#could be large enough and use vertex i so we don't delete it
			else:
				#del usableVertices[i]
				i+=1
				#else:
					#print("neighbors prune")
			
			#else:
				#print("prune")
		return (c[-1],cliques[-1])

#cycle=cycleGenerator(7)
#powerGraph=graphStrongProdPower(cycle,3)
#print(cliquer(cycle))
#print(cliquer(nx.complement(powerGraph)))
#print(cliquer(powerGraph))