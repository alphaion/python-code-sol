import math as m
print('Quadtric Equation: ax² + bx + c  = 0')
a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')
print('Your Equation:',a,'x²',b,'x',c,'= 0')
#implement_shree_dharacharya_formula
#root = (-b±(b²-4ac)**1/2)/2a
f = m.pow(b,2)
g = (((f)-4*a*c)
D = m.pow(g,(1/2))
root1 = (-b+D)/2*a
root2 = (-b-D)/2*a
print('Equation having 2 roots',root1,'and',root2)


