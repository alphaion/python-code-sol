import numpy as np
import math as m
"""
Linear Regression
"""
a = [1,2,3,4,5]
u = [3,4,2,4,5]
"""
To find z = a - ā where ā = mean of a
To find y = u - ū where ū = mean of u
"""
ā = np.mean(a)
ū = np.mean(u)
"""
Make it int(ā) and int(ū)
 """
list_mean_a = []
for i in range(len(a)):
 	z = a[i] - ā
 	list_mean_a.append(z)
print(list_mean_a)
list_mean_u = []
for i in range(len(u)):
	y =str(u[i] - ū)[:4]
	y = float(y)
	list_mean_u.append(y)
print(list_mean_u)
 	
 	

