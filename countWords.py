sentence = list(str(input('Enter Sentence: ')))
n,count = sentence.count(' '), 0
for i in range(len(sentence)):
	count += 1
print('Number of words: ',count-n)
