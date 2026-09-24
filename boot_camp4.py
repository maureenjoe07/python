#randomization and python lists.
import random
random_integer = random.randint(1,10)       #random integer.
print(random_integer)

random_float = random.random()          #random float
print(random_float)

import random
random_choice = random.randint(0,1)

if random_choice == 0:
    print('Heads')
else:
    print('Tails')


#Lista
states_of_nigeria = ['abuja','lagos', 'edo', 'ekiti', 'kano']
print(states_of_nigeria[3])
states_of_nigeria[3] = 'ibadan'         #changing chareacters in list
print(states_of_nigeria)                 
states_of_nigeria.append('kogi')        #adding to list
print(states_of_nigeria)      

import random
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
num_names = len(names)
random_names = random.randint(0, num_names - 1)
result = names[random_names]
print(f'{result} will pay the bill')


line_1 = ["A1", "B1", "C1"]
line_2 = ["A2", "B2", "C2"]
line_3 = ["A3", "B3", "C3"]

map = [line_1, line_2, line_3]
print('Hiding your treasure!X marks the spot.')
position = input('Where do you want to hide your treasure?')


print(f'{line_1}\n{line_2}\n{line_3}')