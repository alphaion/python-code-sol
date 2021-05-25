import random as rndm
List  = [1,2,3,4,5]
list  = []
count = 0
max = max(List)
double = max*2
while len(List) != len(list):
	number = rndm.randint(0,double)
	count+=1
	if number in List:
		number+=1
	else:
		list.append(number)
print(list,'trial at: ',count)
	