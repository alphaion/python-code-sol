# Call of duty, choosing mvp (most valuable player) by kill points.\

import random
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
mvp = []
while (p1+p2+p3+p4+p5) != 50:
    p1=random.randint(1,50)
    p2=random.randint(1,50)
    p3=random.randint(1,50)
    p4=random.randint(1,50)
    p5=random.randint(1,50)
if (p1+p2+p3+p4+p5) == 50:
   print('Player-1 kills: ',p1)
   print('Player-2 kills: ',p2)
   print('Player-3 kills: ',p3)
   print('Player-4 kills: ',p4)
   print('Player-5 kills: ',p5)
mvp.append(p1)
mvp.append(p2)
mvp.append(p3)
mvp.append(p4)
mvp.append(p5)
max = (max(mvp))
print('\nChoosing MVP...')
if (p1==max):
	print('\nPlayer-1 is MVP')
if (p2==max):
	print('\nPlayer-2 is MVP')
if (p3==max):
	print('\nPlayer-3 is MVP')
if (p4==max):
	print('\nPlayer-4 is MVP')
if (p5==max):
	print('\nPlayer-5 is MVP')

	
	
	


