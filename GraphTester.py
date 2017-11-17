from GraphScripts import graphProduct
from GraphScripts import indepSetLP
from GraphScripts import vertexCoverIndep
from GraphScripts import cliqueGenerator

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
	
	
def getGraphBounds(graph, power):
	graphProdMatrix = graphProduct.graphProductPower(graph,power)
	indepSetLPResult = indepSetLP.indepSetLP(graphProdMatrix)
	print("independet set LP relaxation result:")
	print(indepSetLPResult)
	print()
	
	#print(graphProdMatrix)
	vertexCoverIndepResult = vertexCoverIndep.indepSetApprox(graphProdMatrix)
	print("vertex cover result")
	print(vertexCoverIndepResult)
	print()
	
	vertices=[]
	for i in range(len(graphProdMatrix)):
		vertices.append(i)
	
	quantityCliqueResult = cliqueGenerator.quantityCliquesLP(vertices, graphProdMatrix, 10)
	print("Quantity result:")
	print(quantityCliqueResult)
	
	#qualityCliqueResult = cliqueGenerator.qualityCliquesLP(vertices, graphProdMatrix, 0.01)
	#print("Quality result:")
	#print(qualityCliqueResult)
	
def rangeTesting(start, finish, graph):
	for i in range(start, finish+1):
		print("Test for power: "+str(i))
		getGraphBounds(graph, i)
		print("Test for power: "+str(i)+" finished.\n")

def main():
	fileName = sys.argv[1]
	start = int(sys.argv[2])
	finish = int(sys.argv[3])
	
	graph=loadGraphFromFile(fileName)
	
	rangeTesting(start, finish, graph)
	
main()
""""testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
rangeTesting(1,2,testMatrix)

loadGraphFromFile("test.txt")"""