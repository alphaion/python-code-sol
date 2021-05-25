import math
n = int(input('Enter Number of Poster: '))
h = int(input('Enter Arthur\'s height: '))
list_of_height = []
list_of_length = []
for i in range(1,n+1):
    height_of_poster = (input('Height of Poster'+str(i)+': '))
    list_of_height.append(height_of_poster)
for i in range(1,n+1):
    length_of_poster = (input('length of Poster'+str(i)+': '))
    list_of_length.append(length_of_poster)
print('Given height of Poster: ',list_of_height)
max_height_of_poster = max(list_of_height)
indexing=int(list_of_height.index(max_height_of_poster))
print('Given Length of Poster: ',list_of_length)
corresponding_length = int(list_of_length[indexing])
answer = math.ceil((int(max_height_of_poster)-corresponding_length*(1/4))-h)
if answer<=0:
    print(0,'Because Arthur\'s height is enough.')
else:
    print('Height of Ladder: ',answer)





