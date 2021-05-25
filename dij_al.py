start = int(input('Start at: '))
list_val=[]
dis=[]
Num_points=int(input('Number of points: '))
for i in range(1,Num_points+1):
	val=int(input('Value'+str(i)+': '))
	list_val.append(val)
print(list_val)
for k in range(0,len(list_val)):
	while len(list_val)!=0:
		distance=int(input('Distance from',list_val[k],' to ',list_val[k+1],' is: '))
		dis.append(distance)
		k+=1
print(dis)