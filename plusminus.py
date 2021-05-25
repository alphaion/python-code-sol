import math
arr = map(int,input().split())
arr = list(arr)
n_list = []
o_list = []
p_list = []
for i in arr:
    if i<0:
        n_list.append(i)
    if i==0:
        o_list.append(i)
    if i>0:
        p_list.append(i)
print(len(p_list)/len(arr))
print(len(n_list)/len(arr))
print(len(o_list)/len(arr))