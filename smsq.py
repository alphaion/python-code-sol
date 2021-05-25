list1 = []
list2 = []	
for i in range(1,101):
	list1.append(i**2)
for k in range(1,101):
	list2.append(k)
	a = sum(list2)
print((a**2)-(sum(list1)))
	