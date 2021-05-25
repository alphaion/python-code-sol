alice_list = map(int,input().split())
bob_list = map(int,input().split())
listA = list(alice_list)
listB = list(bob_list)
count_A = 0
count_B = 0
count = 0
for i in range(len(listA)):
    if listA[i] == listB[i]:
        count = 0
    if listA[i] > listB[i]:
        count_A +=1
    if listA[i] < listB[i]:
        count_B +=1
print(count_A,count_B)