user = (input())
user = list(user)
for i in range(0,len(user)-1):
    if int(user[i+1])-int(user[i]) == 1:
        print('Yes')
    else:
        print('No')
        