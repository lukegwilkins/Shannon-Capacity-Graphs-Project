import networkx as nx
from vertexOrdering import graphColouringOrder
#cliquer algorithm is based on the algorithm used in cliquer obtained from https://users.aalto.fi/~pat/cliquer.html
#which is licened under GNU General Public License. Created by Sampo Niskanen and Patric R. J. Ostergard

def cliquer(graph):
	
	#We get the vertex ordering
	orderedVertices=graphColouringOrder(graph)
	subsetOfVertices=[]
	c=[]
	cliques=[]
	
	#we calculate each Si
	for i in range(len(orderedVertices)):
		subsetOfVertices.append(orderedVertices[i])
		vertex=orderedVertices[i]
		neighbors=graph.neighbors(vertex)
		usableVertices=[]
		
		for j in neighbors:
			if j in subsetOfVertices:
				usableVertices.append(j)
		
		#if the usable vertices is empty and we have no other cliques then we have a clique of size 1 just the vertex we picked
		if usableVertices==[] and len(c)==0:
			c.append(1)
			cliques.append([vertex])
		#if the amount of use able vertices won't generate a larger clique then we move onto the next vertex
		elif len(usableVertices)+1<=c[-1]:
			c.append(c[-1])
			cliques.append(cliques[-1])
		#else we try to find the maximum clique
		else:
			candidateClique=[vertex]
			clique=cliquerBranching(c,cliques,graph,usableVertices, candidateClique, orderedVertices)
			c.append(clique[0])
			cliques.append(clique[1])

	if(len(cliques)>0):	
		return cliques[-1]
	else:
		return []

		
def cliquerBranching(c,cliques,graph,usableVertices,candidateClique, orderedVertices):
	if usableVertices==[]:
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
						return (c[-1]+1,cliqueSize[1])
					#here we check vertex i but it didn't result in a clique of large enough size, since we explore all
					#sub trees with vertex i we can delete it to remove sub trees which are the same but just a reordering
					#of the vertices in this sub tree
					else:
						del usableVertices[i]
				#here we delete i since the size of the neighbours in the usable vertices isn't large enough to result in
				#a bigger clique
				else:
					del usableVertices[i]
			
			#branches not explored, only thought not worth using vertex, but a clique for a vertex after it in the ordering
			#could be large enough and use vertex i so we don't delete it
			else:
				i+=1
		return (c[-1],cliques[-1])
