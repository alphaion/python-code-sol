limit,k = map(int,input().split())
array = map(int,input().split())
array = list(array)
new=[]
for i in range(0,len(array)):
	for j in range(0,len(array)):
		if i<j and (array[i]+array[j])%k==0:
			new.extend([[i,j]])
print(len(new))