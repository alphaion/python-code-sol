sum = 0
sums = 0
x = map(int,input().split())
x = list(x)
x.sort()
for i in range(len(x)-1):
    sum += x[i]
for k in range(len(x)):
    sums += x[k]
print(sum,sums-x[0])

    