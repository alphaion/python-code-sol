x = input()
x = list(x)
for i in range(0,len(x)-1):
	if x[i]==x[i+1]:
		x[i+1]='*'
print(x)