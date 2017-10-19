from GraphScripts import graphProduct
from GraphScripts import indepSetLP

def getGraphBounds(graph, power):
	graphProdMatrix = graphProduct.graphProductPower(graph,2)
	indepSetLPResult = indepSetLP.indepSetLP(graphProdMatrix)
	
	
testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
getGraphBounds(testMatrix,2)