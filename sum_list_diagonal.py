limit = int(input())
a = map(int,input().split())
b = map(int,input().split())
c = map(int,input().split())
a = list(a)
b = list(b)
c = list(c)
diagonal_1 = a[0]+b[1]+c[2]
diagonal_2 = a[-1]+b[-2]+c[-3]
print(diagonal_1+diagonal_2)
