list = []
def perfect_number(number):
	for i in range(1,number):
		if number%i==0:
			list.append(i)
			if sum(list)==number:
				print(number,'is a perfect number.')
def main():
	number = int(input())
	output=perfect_number(number)
if __name__ =='__main__':
	main()