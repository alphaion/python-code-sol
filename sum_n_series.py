#NUMBER_OF_INPUT
list_Tn = []
number_of_input=int(input())
for i in range(number_of_input):
    new_number=int(input())
    for k in range(1,new_number+1):
        Tn=(k**2)-((k-1)**2)
        list_Tn.append(Tn)
print(sum(list_Tn))