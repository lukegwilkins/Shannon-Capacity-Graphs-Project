from GraphScripts import graphProduct
from GraphScripts import indepSetLP

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
	
	for i in matrix:
		print(i)
	
	
def getGraphBounds(graph, power):
	graphProdMatrix = graphProduct.graphProductPower(graph,2)
	indepSetLPResult = indepSetLP.indepSetLP(graphProdMatrix)
	print(indepSetLPResult)
	
	
testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
getGraphBounds(testMatrix,2)

loadGraphFromFile("test.txt")