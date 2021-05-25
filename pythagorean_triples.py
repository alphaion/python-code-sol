n = int(input())
for k in range(1,n):
    for i in range(1,n):
        for j in range(1,n):
            if i+j+k == n:
                if (i**2)+(j**2)==(k**2):
                        print(str(i)+'^2 + ',str(j)+'^2 = ',str(k)+'^2')

                
        