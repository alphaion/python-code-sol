limit=int(input())
arr=[]
for a in range(limit):
	ar = int(input())
	arr.append(ar)
m = []
for i in arr:
	while i%5!=0:
		i+=1
		if i%5==0:
			m.append(i)
			
"""m= list of multiple of 5"""

new=[]
for k in range(len(m)):
	if m[k]-arr[k]<3 and arr[k]>=38:
		new.append(m[k])
	else:
		new.append(arr[k])
print(*new,sep='\n')