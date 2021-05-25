import math
s1 = float(input('First Side: '))
s2 = float(input('Second Side '))
s3 = float(input('Third Side '))
a = ((s1+s2+s3)/2)
b = (a*(a-s1)*(a-s2)*(a-s3))
z = math.pow(b,(1/2))
print ('Area of Δ: ',z)
    