from copy import copy

def incrementClique(graph,clique):
	vertex=clique[0]
	cliques = []
	cliques.append(clique)
	for i in range(len(graph[vertex])):
		if i not in clique:
			newVertex=True
			j=0
			while j<len(clique) and newVertex:
				if graph[i][clique[j]]==0:
					newVertex=False
				j+=1
			if newVertex:
				newClique=copy(clique)
				newClique.append(i)
				cliques.append(newClique)
	return cliques
matrix=[[1,1,1],[1,1,1],[1,1,1,]]
cliques=incrementClique(matrix,[0])
print(cliques)