arr = map(int,input().split())
arr = list(arr)
ma = []
mi = []
eq = []
#FIND THE smaller

for i in range(0,len(arr)-1):
    if arr[i]<arr[i+1]:
       mi.append(arr[i])
print("Min: ",mi)

#find the greater

for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
       ma.append(arr[i])
print("Max: ",ma)

#find equal

for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
       eq.append(arr[i])
print("Equal: ",eq)
