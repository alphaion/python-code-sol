import math as m
import datetime
import time
class bc:
    red="\033[31m"
    green="\033[32m"
    blue="\033[34m"
    cyan="\033[36m"
    lightblue="\033[94m"
    lightcyan="\033[96m"
    end="\033[0m"
    bold="\033[1m"
print(bc.lightcyan+'Welcome To The Termux.\n\n'+bc.end,bc.green+'I\'m LARA ( Logrithm Aritificial Regulated Assistance )'+bc.end)
print('\nAuthor : '+bc.red+'Rishabh'+bc.end)
user_name = str(input('\nWhat Should I call you:\t'))
if type(user_name) == str:
    print('\nHye!',user_name,' Nice to meet you.')
print('\nToday Date and Time is:' ,datetime.datetime.now())
print('\nWhat Can I do for you\n\nHere are some keywords::-> Enter serial No. only.\n\n1.Add\n2.Sub\n3.Multi\n4.Division\n5.Area\n6.Trigonometry\n7.Square root\n8.Cube root\n9.Log\n10.Guess Games with LARA\n11.Cricket with LARA\n12.Rock, Paper, Scissor ')
user_task = str(input('\nEnter Your Task: '))
if user_task == '1':
    number_add = int(input('How many Number you wanna Add: '))
    total_num_add = 0
    print('Enter Your Numbers ')
    for i in range(1, number_add + 1):
        numberadd = float(input('Number'+str(i)+': '))
        assert numberadd>=0 and numberadd<=999999999
        total_num_add += numberadd
        print(total_num_add)
elif user_task == '2':
    print('Enter Your Number')
    numsub_a = int(input('Number 1: '))
    numsub_b = int(input('Number 2: '))
    sub = numsub_a- numsub_b
    print('The answer is:',sub)
elif user_task == '3':
    nummulti_a = float(input('Number 1: '))
    nummulti_b = float(input('Number 2: '))
    multi = nummulti_a*nummulti_b
    print('The answer is: ',multi)
elif user_task == '4':
    numdivi_a=float(input('Number 1: '))
    numdivi_b=float(input('Number 2: '))
    divi = numdivi_a/numdivi_b
    print('The answer is: ',divi)
     # AREA OF Shape START #
elif user_task=='5':
    print('\nArea of triangle(tri), Rectangle(rect), Square(sq)')
    area1 = str(input('\nEnter your shape: '))
    if area1 == 'tri':
      s1 = float(input('\nFirst Side: '))
      s2 = float(input('\nSecond Side '))
      s3 = float(input('\nThird Side '))
      a = ((s1+s2+s3)/2)
      b = (a*(a-s1)*(a-s2)*(a-s3))
      z = m.pow(b,(1/2))
      print ('\nArea of Δ: ',z,'sq unit')
    elif area1 == 'rect':
          side_rect_l = float(input('\nEnter Length: '))
          side_rect_b = float(input('\nEnter breadth: '))
          area_rect =  side_rect_l* side_rect_b
          print('\nArea of rectangle is: ',area_rect,'sq unit')
    elif area1 == 'sq':
          side_sq = float(input('\nEnter Side: '))
          area_sq =  side_sq**2
          print('\nArea of square is: ',area_sq,'sq unit')
     # AREA OF Shape END #
elif user_task == '6':
    angle = int(input('Enter Angle: '))
    assert angle>=0 and angle<=360
    trigonometric = str(input('Enter sin or cos or tan: '))
    if trigonometric =='sin':
        sin = m.sin(angle)
        print('The value of sin',angle, '= ',sin)
    elif trigonometric =='cos':
        cos = m.cos(angle)
        print('The value of cos',angle, '= ',cos)
    elif trigonometric =='tan':
        tan = m.tan(angle)
        print('The value of tan',angle, '= ',tan) 
elif user_task == '7':
    sqr_a = float(input('Enter Number: '))
    sq_ra = (sqr_a**(1/2))
    print('Square root of ',sqr_a,'is: ',sq_ra)
elif user_task == '8':
    cbr_a = float(input('Enter Number: '))
    cb_ra = (cbr_a**(1/3))
    print('Cube root of ',cbr_a,'is: ',cb_ra)
elif user_task == '9':
    log_val = float(input('Enter Number: '))
    log = m.log(log_val)
    print('The value of log(',log_val,') is: ',log)
elif user_task == '10':
    print('Welcome in my Game zone.',user_name,)
    print('Computer number = x, you will have to find x. Can You do?')      
    import random
    computer_guess = random.randint(1, 100)
    user_input = ''
    tries = 0
    while user_input != computer_guess:
    	
        user_input = int(input('Guess the number: '))
        tries+=1
        if user_input > computer_guess:
             print('High! Guess Again')
        elif user_input < computer_guess:
             print('Low! Guess Again')
        else:
             print('Yeah You got it.You took',tries,'tries.Try again for less.')
elif user_task=="11":
       import random
       print("This cricket game is created by ALEX.")
       player_name=str(input("Enter your name:"))
       player_score=0
       player_bat=0
       computer_bowling=random.randint(1,6)
       while computer_bowling != player_bat:
           player_bat=int(input("Enter your  run:"))
           if player_bat>6:
              print("Please only choose between 0 to 6.")
              player_score-=player_bat
           computer_bowling=random.randint(1,7)    
           player_score=int(player_score)
           computer_bowling=int(computer_bowling)
           if computer_bowling==player_bat:
            print(player_name,"You are out!,Your total score is",player_score)
           else:
            player_score +=player_bat
            print("You hitted",player_bat,"Your score is",player_score)
            continue
       computer_score=0
       player_bowling=0
       computer_bating=random.randint(1,7)
       while computer_score <= player_score or computer_bating!=player_bowling:
        player_bowling=int(input("Enter your bowling:"))
        computer_bating=random.randint(1,7)
        player_bowling=int(player_bowling)
        computer_score=int(computer_score)
        computer_bating=int(computer_bating)
        if computer_bating==player_bowling:
            print("Its out! well done!",player_name,"you win!")
            break
        elif computer_score>=player_score:
            print(player_name,"You lose! Better Luck next time. ")
            break
        else:    
             computer_score+=computer_bating
             print("Opponent hitted",computer_bating,"Total score is",computer_score,",",player_score-computer_score,"is needed by opponent to win")
             continue
        Exit=input("press enter to exit")
elif user_task=="12":
    import random
    player_name=str(input("Hey,what's your name:"))
    if player_name=="sarvesh":
        print("Hello! lets check this programme function")
    else:
        print(player_name,"Welcome! Lets play this game:)")
    game_time=int(input("how many times you want to play:"))
    you_won=0
    computer_won=0
    while game_time!=0:
        computer_choice=random.randint(1,3)
        player_choice=str(input("Enter your choice(r/p/s):"))
        if computer_choice==1:
            computer_choice="r"
        elif computer_choice==2:
            computer_choice="p"
        elif computer_choice==3:
            computer_choice="s"
        print("computer choosed:",computer_choice)
        if player_choice=="r" and computer_choice=="s":
            print("You Win!")
        elif player_choice=="p" and computer_choice=="r":
            print("You win!")
        elif player_choice=="s" and computer_choice=="p":
            print("You Win!")
            you_won=int(you_won)
            you_won=you_won+1
        elif computer_choice==player_choice:
            print("Its tie")
        else:
            print("You Lose!")
            computer_won=int(computer_won)
            computer_won=computer_won+1
        game_time=game_time-1        
    print("You won",you_won,"computer won",computer_won)
    if you_won>computer_won:
        print(player_name,"Wow!,You Won,You proved Humans are superior to Lara ")
    elif you_won==computer_won:
        print(player_name,"its draw! are we coming near to technological singularity.")
    else:
        print(player_name,"YOU FOOL! You lost to a Lara!")
    getexit=input("press enter to exit")
print('\nEnd of Program!! Run me again',user_name,'Bye-~~-Bye')

                    
                    
                    
                    
                    
                    
                    
                    
                    