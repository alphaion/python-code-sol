x=(int(input('enter ')))
y=list(range(1,x+1))
byes=0
byes_from=[2,4,8,16,32]
byes_form_index=[0,-1,1,-2,2,-3,3,-4,4,-5]
print("Team in Fixture",y)
upper_half=y[0:int(((len(y)+1)/2))]
print("Upper Half:",upper_half)
lower_half=y[int(((len(y)+1)/2)):]
print("Lower Half:",lower_half)
for i in byes_from:
	if x>i and x< byes_from[byes_from.index(i)+1]:
	 		byes=byes_from[byes_from.index(i)+1]-x
print("Byes=",byes)
def give_byes(byes):
	for  i in byes_form_index:
		  if byes !=0:
		  	lower_half.remove(lower_half[i])
		  	lower_half.insert(i,"Byes")
		  	byes-=1
		  else:
		  	   return 
		  if byes !=0:
		  	j=-i
		  	upper_half.remove(upper_half[j])
		  	upper_half.insert(i,"byes")
		  	byes-=1
		  else:
		    	return
give_byes(byes)
print(upper_half)
print(lower_half)