#Higher or lower game.
import random
import time
dict_list= [
    {'A': 5000},
    {'B': 1000},
    {'C': 34000},
    {'D': 10100},
]
print('Guess which has a higer number!')
choice_A = random.choice(dict_list)
#print(choice_A)
for key in choice_A:
    option_A = (choice_A[key])
#print(option_A)

choice_B = random.choice(dict_list)
if choice_B == choice_A:
    choice_B = random.choice(dict_list) 
#print(choice_B)
for key in choice_B:
    option_B = (choice_B[key])
#print(option_B)

choice = input('Type "A" to chose option A and "B" to chose option B: ').upper()

end_game = False
while end_game == False:
    if option_A > option_B and choice == 'A':
        output = 'Correct!'
        print(output)
        print(f'option_A = {option_A} \n option_B = {option_B}')
    elif option_B > option_A and choice == 'B':
        output = 'Correct!'
        print(output)
        print(f'option_A = {option_A} \n option_B = {option_B}')
    else:
        output = 'Incorrect!'
        print(output)
        print(f'option_A = {option_A} \n option_B = {option_B}')

    #print(output)
    if output == 'Correct!':
        option_A = option_B
        #print(option_A)
        choice_B =  random.choice(dict_list)
        for key in choice_B:
            option_B = (choice_B[key])
        #print(option_B)
        if option_B == option_A:
            choice_B = random.choice(dict_list) 
            #print(choice_B)
        for key in choice_B:
            option_B = (choice_B[key])
        #print(option_B)
        time.sleep(2)
        choice = input('Type "A" to chose optiBn A and "B" to chose option B: ').upper()
    else: 
        end_game = True
        print('Game over!')