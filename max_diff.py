a = int(input())
x = map(int, input().split())
x = list(x)
m = max(x)
arr = []
for i in range(m):
     if i in x:
          diff = (m-i)
          arr.append(diff)
print(max(arr))