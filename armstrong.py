def armstrong(x):
	x=str(x)
	sum=0
	for i in range(len(x)):
		sum+=(int(x[i]))**3
	if int(x)==sum:
		print(x)
	else:
		  return
lower=int(input("Enter lowest range:"))
higher=int(input("Enter higher range:"))
print("Armstrong number btween",lower,"and",higher,"are")
for x in range(lower,higher+1):
	armstrong(x)
