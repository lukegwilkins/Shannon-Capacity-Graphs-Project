import numpy as np
from copy import copy
from GraphScripts import cliqueGenerator
def ternary(n):
	if n==0:
		return '0'
	nums =[]
	while n:
		n,r=divmod(n,3)
		nums.append(str(r))
	return ''.join(reversed(nums))


def neighbours(k):
	vertices=[]
	for i in range(0,3**k):
		vertices.append(ternary(i).zfill(k))
	return vertices

def connected(u,v):
	for i in range(len(u)):
		if((u[i]=='2' and v[i]=='0') or (u[i]=='0' and v[i]=='2')):
			return False
	return True
	
def subgraph(k):
	vertices=neighbours(k)
	#print(vertices)
	graph=np.ones((len(vertices),len(vertices)), dtype=np.int)
	
	for i in range(len(vertices)):
		for j in range(i+1,len(vertices)):
			print(vertices[i])
			print(vertices[j])
			print(connected(vertices[i],vertices[j]))
			print()
			if not connected(vertices[i],vertices[j]):
				graph[i][j]=0
				graph[j][i]=0
	
	for i in graph:
		print(i)
		
def baseClique(k):
	baseClique=[]
	for i in range(2**k):
		x=bin(i)[2:].zfill(k)
		baseClique.append(x)
	return baseClique
	
def replaceVertices(baseClique, vertices):
	clique=[]
	for baseVer in baseClique:
		vertex=""
		for j in range(len(baseVer)):
			vertex=vertex+str(vertices[j][int(baseVer[j])])+", "
		vertex=vertex[:-2]
		clique.append(vertex)
	return clique

def addElementToLists(k, lists):
	returnLists=[]
	for i in lists:
		returnLists.append([k]+i)
	return returnLists

def subLists(list,k):
	if k==1:
		returnSubLists=[]
		for i in list:
			returnSubLists.append([i])
		return returnSubLists
	else:
		returnSubLists=[]
		for i in list:
			tempList=copy(list)
			tempSubLists=subLists(tempList,k-1)
			returnSubLists=returnSubLists+addElementToLists(i, tempSubLists)
		return returnSubLists

def convertClique(clique, n):
	convertedClique=[]
	for i in clique:
		vertexData=i.split(",")
		power=0
		vertex=0
		for i in vertexData:
			vertex=vertex+int(i)*(n**power)
			power+=1
		convertedClique.append(vertex)
	return convertedClique
	
def cycleCliques(n,k):
	partitions=[]
	for i in range(n):
		partOne=[i,(n+(i-1))%n]
		partTwo=[i, (i+1)%n]
		partitions.append(partOne)
		partitions.append(partTwo)
	
	vertexSubLists=subLists(partitions,k)
	#print(vertexSubLists)
	
	cliqueBase= baseClique(k)
	cliques=[]
	for i in vertexSubLists:
		cliques.append(convertClique(replaceVertices(cliqueBase, i),n))
	
	vertices=[]
	for i in range(n):
		vertices.append(i)
	
	powerVers=verticesInGraphRec(vertices,k)
	#print(cliques)
	#print()
	#print(powerVers)
	
	return cliqueGenerator.createAndRunLP(cliques,powerVers)

def verticesInGraphRec(vertices, power):
	if power <=1:
		returnList=[]
		for v in vertices:
			returnList.append(str(v))
		return returnList
	else:
		subSequence = verticesInGraphRec(vertices, power-1)
		newVertices=[]
		for v in vertices:
			for sequence in subSequence:
				newVertices.append(str(v)+","+sequence)
		return newVertices
		
def convertCliqueTester(n,k):
	vertices=[]
	for i in range(n):
		vertices.append(i)
	
	powerVers=verticesInGraphRec(vertices,k)
	
	for i in powerVers:
		print(convertClique([i],n))
		
def main(filename):
	file=open(filename,'w')
	k=1
	for i in range(5,47,2):
		print("Cycle size is "+str(i)+" power is "+str(k))
		fractIndep=cycleCliques(i,k)
		print("fractional indept set is "+str(fractIndep))
		print("So independet set in k=2 is "+str(int(((i//2)*fractIndep))))
		file.write(str(i)+", "+str(fractIndep)+", "+str(int(((i//2)*fractIndep)))+"\r\n")
	file.close()
		
filename="results/cycles5to45.txt"
main(filename)