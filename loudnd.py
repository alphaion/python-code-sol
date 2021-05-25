inp = map(int,input().split())
inp = list(inp)
mul = int(inp[0])*int(inp[1])
l = []
for i in range(1,mul):
	z = mul-i
	l.append(z)
print(max(l))
	