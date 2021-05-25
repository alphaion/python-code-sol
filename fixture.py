a = int(input('Enter_no._of_Teams: '))
print ('Matches:', a-1)
#first_loop_for_up_&&_lower_half
if a%2 == 0:
  print ('Upper Half:', (a/2))
  print ('Lower Half:', (a/2))
else:
 print ('Upper Half:', (a+1)/2)
 print ('Lower Half:', (a-1)/2)
#second_loop_for_calc_byes_rounds
if a < 4:
   print ('Byes:', 4-a)
   print ('Rounds: 2')
elif a<8:
   print ('Byes:', 8-a)
   print ('Rounds: 3')
elif a<16:
   print ('Byes:', 16-a)
   print ('Rounds: 4')
elif a<32:
	print ('Byes:', 32-a)
	print ('Rounds:5')
elif a<64:
	print ('Byes:', 64-a)
	print ('Rounds:6')
elif a<128:
	print ('Byes:', 128-a)
	print ('Rounds:7')
elif a<256:
	print ('Byes:', 256-a)
	print ('Rounds:8')
elif a<512:
	print ('Byes:', 512-a)
	print ('Rounds:9')
elif a<1024:
	print ('Byes:', 1024-a)
	print ('Rounds:10')