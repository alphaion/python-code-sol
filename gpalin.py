a = []
for i in range(100,1000):
	for k in range(100,1000):
		mul = i*k
		a.append(mul)   
		for j in a:
    	    s = map(str,a)
     	   s = ''.join(s)
 		   s = list(s)           # 123
			if s[::-1]==s[0::]:
				print(s)
		
	