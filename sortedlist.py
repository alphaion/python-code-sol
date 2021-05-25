def selectionSort(list):
	'''To Sort the list in ascending order using selection sort'''
	for i in range(0,len(list)-1):
		minIndex = i
		for j in range(i+1,len(list)):
			if list[j] < list[minIndex]:
				minIndex = j
			if minIndex != 1:
				list[minIndex],list[i] = list[i],list[minIndex]
def main():
	list = [8,3,2,4,3,2,5]
	print('Entered List',list)
	selectionSort(list)
	print('Sorted List',list)
if __name__=='__main__':
	main()