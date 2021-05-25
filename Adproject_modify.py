print('Enter Matrix A')
row_1A = []
row_2A = []
row_3A = []
for i in range(1,4):
	R1 = int(input('Enter Element of Row '+str(i)+ ' Column 1 = '))
	row_1A.append(R1)
for i in range(1,4):
	R2 = int(input('Enter Element of Row '+str(i)+ ' Column 2 = '))
	row_2A.append(R2)
for i in range(1,4):
	R3 = int(input('Enter Element of Row '+str(i)+ ' Column 3 = '))
	row_3A.append(R3)
print('Matrix A is :')
#print(row_1A,'\n',row_2A,'\n',row_3A)
matA = [row_1A] + [row_2A] + [row_3A]
print('\n',matA)
#Matrix B
print('\n\nEnter Matrix B')
row_1B = []
row_2B = []
row_3B = []
for i in range(1,4):
	R1 = int(input('Enter Element of Row '+str(i)+ ' Column 1 = '))
	row_1B.append(R1)
for i in range(1,4):
	R2 = int(input('Enter Element of Row '+str(i)+ ' Column 2 = '))
	row_2B.append(R2)
for i in range(1,4):
	R3 = int(input('Enter Element of Row '+str(i)+ ' Column 3 = '))
	row_3B.append(R3)
print('Matrix B is :')
#print(row_1B,'\n',row_2B,'\n',row_3B)
matB = [row_1B] + [row_2B] + [row_3B]
print('\n',matB)
"""Here comes the Pain
Result = Matrix A * Matrix B"""
result = [[0,0,0],[0,0,0],[0,0,0,]]
for p in range(len(matA)):
	for q in range(len(matB[0])):
		for r in range(len(matB)):
			result[p][q] += matA[p][r]*matB[r][q]
for z in result:
	print('Multiplication of Matrix A and Matrix B is :',z)






	
	
	