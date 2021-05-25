from sympy import isprime
digit = []
ddigit = []
tdigit = []
ddprime = []
tdprime = []
list_for_tdprime = []
list_for_ddprime = []
o_s = []
for i in range(10,1000):
	digit.append(i)
for i in digit:
	if len(str(i)) == 2:
		ddigit.append(i)
	if len(str(i)) == 3:
		tdigit.append(i)
for prime in ddigit:
	if isprime(prime) == True:
		ddprime.append(prime)
for primes in tdigit:
	if isprime(primes) == True:
		tdprime.append(primes)
for k in ddprime:
	if '1' not in str(k) and '7' not in str(k):
		list_for_ddprime.append(k)
print(list_for_ddprime)
for k in tdprime:
	if '1' not in str(k) and '7' not in str(k):
		list_for_tdprime.append(k)
print(list_for_tdprime)
