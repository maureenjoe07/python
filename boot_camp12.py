#NAME SPACES: local and global spaces.
#logo
logo = r""" 
 _____ _             _____                       _                _____                      
|_   _| |__   ___   / ____|_   _  ___  ___ ___ _(_)_ __   __ _  / ____| __ _ _ __ ___   ___ 
  | | | '_ \ / _ \ | |  __| | | |/ _ \/ __/ __| | | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
  | | | | | |  __/ | |__| | |_| |  __/\__ \__ \ | | | | | (_| | | |__| |(_| | | | | | || __/
  |_| |_| |_|\___|  \_____|\__,_|\___||___/___/_|_|_| |_|\__, | \____  \__,_|_| |_| |_| \___|
                                                           ___/                             
"""
print(logo)
#welcome player
import random
print('Welcome to the number guessing game!')

#chose a level and give attempt accordingly
level = input('Pls chose a level of difficulty (E-easy and H-hard):  ').lower()
if level == 'e':
    attempt = 10
    print(f'You have {attempt} attempts to guess the number.')
else:
    attempt = 5
    print(f'You have {attempt} attempts to guess the number.')

#tell them i'm guessing a umber between 1-100
my_thinking = random.randint(1,100)
print("i'm thinking of a number between 1-100.")

#lwt them make guesses
guess = False
while guess == False:
    if attempt > 0:
        your_guess = int(input('Try to guess the number: '))
        if your_guess > my_thinking:
            print('Too high.')
            attempt -= 1
            print(f'You have {attempt} attempts left')
        elif your_guess < my_thinking:
            print('Too low.')
            attempt -= 1
            print(f'You have {attempt} attempts left')
        elif your_guess == my_thinking:
            guess = True
            print('You guessed correct!\n You win!')
    else:
        guess = True
        print(f"you've run out of attempt. \n The number is {my_thinking}.")
