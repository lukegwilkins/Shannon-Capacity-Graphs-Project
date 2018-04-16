import numpy as np
def csvToMatrix(filename):
	matrix=[]
	file=open(filename,"r")
	data=file.read()
	datalines=data.split("\n")
	for line in datalines:
		if "," in line:
			row=[]
			lineData=line.split(",")
			for entry in lineData:
				row.append(int(entry))
			matrix.append(row)
	return matrix
	
def adjMatrixToB(adjMatrix):
	#n=len(adjMatrix)
	#m=len(adjMatrix[0])
	#b= np.ones((n,m))
	count=1
	for i in range(len(adjMatrix)):
		for j in range(i,len(adjMatrix[i])):
			if(adjMatrix[i][j]==0):
				adjMatrix[i][j]="M"+str(count)
				adjMatrix[j][i]=adjMatrix[i][j]
				count+=1
			else:
				adjMatrix[i][j]=0
				adjMatrix[j][i]=adjMatrix[i][j]
			
	return adjMatrix

mat=csvToMatrix("paley5.csv")
for i in mat:
	print(i)
print()

bMat=adjMatrixToB(mat)
for i in bMat:
	print(i)
	
#bMatrixToLP(bMat)