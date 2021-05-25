a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
new_list = []
if (a%2!=0) and (b%2!=0):
	for i in range(a,b+1):
		if (i%2!=0):
			new_list.append(i)
print(new_list)