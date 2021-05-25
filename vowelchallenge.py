given_arr = ['a','e','i','o','u']
user = list(input())
count = 0
for i in range(len(user)):
    if user[i] in given_arr:
       count+=1
print(count)