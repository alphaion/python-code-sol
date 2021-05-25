count = []
import random
list = []
x = [1,2,3,4,5]
while len(x)>=len(list):
    ran = random.randint(min(x),max(x))
    list.append(ran)
    print(list)
    list.count(ran)
    if count(ran>1):
        list.append(ran)
        print(list)