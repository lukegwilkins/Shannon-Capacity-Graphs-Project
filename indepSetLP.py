import numpy as np
from scipy.optimize import linprog
from graphProduct import graphProductPower

#function to generate the LP which would calculate the fractional independent set of
#a graph. The input to the function is an adjacency Matrix (2d array), and a boolean
#which is true if the linear program solver you are using is a minimizer, and false
#otherwise
def indepSetLP(adjacencyMatrix, lpIsMinimizer):
	#gets the size of the graph
	n = len(adjacencyMatrix)
	#figures out how many edges are in the graph, we only need to do each edge once
	noOfEdges=(np.sum(adjacencyMatrix)-n)//2
	#print(noOfEdges)
	#creates the matrix to store A, check if need dtype=np.int
	matrixA = np.zeros((noOfEdges,n))
	
	#figures out which line in A we are changing
	matrixLine=0
	
	#for each vertex in the adjacency matrix it checks which vertices it is adjacent to
	#then for each one we make a new constraint where vertex i + vertex j <=1
	for i in range(n):
		#we start at i+1 since we don't need to do those edges as they are already
		#covered in another constraint, also each vertex is connected to itself so 
		#we can skip that to
		for j in range(i+1, n):
			#if there is an edge between i and j then matrixA is changed to include
			#that constraint
			if adjacencyMatrix[i][j]==1:
				matrixA[matrixLine][i]=1
				matrixA[matrixLine][j]=1
				#once we have made this constraint we increment matrixLine to move onto the next one
				matrixLine+=1
	
	#figures out the upper bounds for each constraint, rather easy here since they all have to be <=1
	constraintUpperBounds = np.ones(noOfEdges)	
	
	#the objective function is also easy since it is all 1s, however if the linear program solver
	#is a minimizer then we times it by -1 to make sure it is all -1s
	if lpIsMinimizer: 
		objFunction = -1*np.ones(n)
	else:
		objFunction = np.ones(n)
		
	bounds=(0,1)
	return objFunction, matrixA, constraintUpperBounds, bounds


testMatrix=[[1, 1, 0, 0, 1],[1, 1, 1, 0, 0],[0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]

graphProdMatrix = graphProductPower(testMatrix,2)
#print(len(graphProdMatrix[1]))
#for i in graphProdMatrix:
	#print(i)
#testMatrix=[[1,1,0],[1,1,1],[0,1,1]]
objFunction, matrixA, constraintUpperBounds, variableBounds=indepSetLP(graphProdMatrix, True)
#print(objFunction)
#print(matrixA)
#print(constraintUpperBounds)
#print(variableBounds)

res = linprog(objFunction, A_ub=matrixA, b_ub= constraintUpperBounds, bounds=variableBounds)

print(res)