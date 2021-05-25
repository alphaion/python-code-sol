import random
computer_guess = random.randint(1,100)
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
           
           
          
      
         