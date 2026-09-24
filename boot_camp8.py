# FUNCTIONS WITH INPUT.
#Regular function.
def greet():
    print('Good day to you!')
    print('How was your day?')
    print('Ok then....rest up and try again tomorrow')

greet()

# #Function with input.
def greet_with_name(name):
    print(f'Good day to you {name}!')
    print(f'How was your day {name}?')
    print(f'Ok then {name}....rest up and try again tomorrow')

greet_with_name('Maureen')

# Function with multiple input.
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'what is it like in {location}?')

greet_with('Maureen', 'Lagos')          #positional argument.
greet_with(location= 'Lagos', name='Maureen')

#CHALLANGE.
import math 

def paint_calc( height, width, coverage):
    test_h = int(input('What is the height of your wall?\n'))
    test_w = int(input('What is the width of your wall?\n'))
    cover =  5 
    cans_needed = (test_h * test_w) / cover
    round_up_cans = math.ceil(cans_needed)
    print(f'You need {round_up_cans} cans of paint to paint your wall')

paint_calc(height = 'test_h', width = 'test_w', coverage = 'cover')

#CHALLANGE 2.
def prime_cheacker(number):
    prime_number = True
    for i in range(2, number):
        if number % i == 0:
            prime_number  = False
    if prime_number == True:
        print(f'{number} is a prime')
    else:
        print(f'{number} is not a prime')
     
n = int(input('Pls enter the number you want to check.'))

prime_cheacker(number = n)

#CHALLANGE 3.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n')
text = input('Type your message: \n').lower()
shift = int(input('Type the shift number: \n'))

def ceaser(text, shift, direction):
    output = '' 
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = (position + shift) % 26
                output += alphabet[new_position]
            else:
                back_position = (position - shift) % 26
                output += alphabet[back_position]
        else:
            output += char
    print(output)  

ceaser(text= text, shift= shift, direction= direction)

end_game = False
while end_game == False:
    decision = input('Do you want to go again?')
    if decision == 'yes':
        direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n')
        text = input('Type your message: \n').lower()
        shift = int(input('Type the shift number: \n'))
        ceaser(text= text, shift= shift, direction= direction)
    else:
        end_game = True
        print('Goodbye.')

# def encode(text, shift):
#     if direction == 'encode':
#         output = ''
#         for letter in text:
#             position = alphabet.index(letter) 
#             new_position = (position + shift) % 26
#             output += alphabet[new_position] 
#         print(output)       

# def decode(text, shift):
#     if direction == 'decode':
#         output = ''
#         for letter in text:
#             position = alphabet.index(letter) 
#             back_position = (position - shift) % 26
#             output += alphabet[back_position] 
#         print(output)       

# if direction == 'encode':
#     text = input('Type your message: \n').lower()
#     shift = int(input('Type the shift number: \n'))
#     encode(text = text, shift = shift)
# elif direction == 'decode':
#     text = input('Type your message: \n').lower()
#     shift = int(input('Type the shift number: \n'))
#     decode(text = text, shift = shift)    
# else:
#     print('Invalid input!') 
