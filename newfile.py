import math as m
print('Hey!! user, My name is M.A.I.T and I am A.I. designed by my Boss.')
user_name = str(input('What Should I call you: '))
print('Hey!!',user_name,'Nice to meet you.')
print('What Can I do for you\nHere are some keywords: add, sub, multi, division, trigonometry\n Or Do you wanna play games like cricket and rock paper scissor for that type (cricket or rps)')
user_task = str(input('Enter Your Task: '))
if user_task == 'add':
    number_a = int(input('How many Number you wanna Add: '))
    total_num = 0
    print('Enter Your Numbers ')
    for i in range(1, number_a + 1):
        number = float(input('Number'+str(i)+': '))
        assert number>=0 and number<=999999999
        total_num += number
        print(total_num)
elif user_task == 'sub':
    print('Enter Your Number')
    num_b = int(input('Number 1: '))
    num_c = int(input('Number 2: '))
    sub = num_b - num_c
    print('The answer is:',sub)
elif user_task == 'multi':
    num_m1 = float(input('Number 1: '))
    num_m2 = float(input('Number 2: '))
    multi = num_m1 * num_m2
    print('The Answer is: ',multi)
elif user_task == 'division':
    num_d1=float(input('Number 1: '))
    num_d2=float(input('Number 2: '))
    divi = num_d1/num_d2
    print('The answer is: ',divi)
elif user_task == 'trigonometry':
    angle = int(input('Enter Angle: '))
    assert angle>=0 and angle<=360
    trigono = str(input('Enter sin or cos or tan: '))
    if trigono =='sin':
        sin = m.sin(angle)
        print('The value of sin',angle, '= ',sin)
    elif trigono =='cos':
        cos = m.cos(angle)
        print('The value of cos',angle, '= ',cos)
    elif trigono =='tan':
        tan = m.tan(angle)
        print('The value of tan',angle, '= ',tan)
elif user_task=="cricket":
    import random
    print("This cricket game.")
    player_name=user_name
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
import random
player_name = user_name
if player_name=="Boss":
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
     print(player_name,"Wow!,You Won,You proved Humans are superior to BOT! ")
elif you_won==computer_won:
     print(player_name,"its draw! are we coming near to technological singularity.")
else:
     print(player_name,"YOU FOOL! You lost to a BOT!")
     getexit=input("press enter to exit")
                    
                    
                    
                    
                    
                    
                    
                    
                    