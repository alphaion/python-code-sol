take = map(int,input().split())
take = list(take)
b = take[0]
a = take[1]
z = 2*a
while (z%b!=0):
	z+=1
print(z//b)