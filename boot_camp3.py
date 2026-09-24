# conditional statements, logical operators, code blocks and sscope.
print('Welcome to the roller coaster ride!')
height = int(input('Please enter your height.\n'))

if height >= 120:
    print('tall enough to ride.')
else:
    print('too short to ride.')

age = int(input('what is your age?'))

if age >= 18:
    print('your ride will cost #12.')
elif age <= 12:
    print('your ride will cost #5.')

#coding excercise (checking for even and odd numbers), nested if statement..
number = int(input('enter a number.\n'))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')


year = int(input('enter a year.\n'))

if year % 4 == 0:
    if  year % 100 == 0:
        if  year % 400 == 0:
         print(f'{year} is a leap year')   
        else:
            print(f'{year} is not a leap year')
    else:
      print(f'{year} is not a leap year')
else:
   print(f'{year} is not a leap year')



print('Thank you for choosing python pizza deliveries!')
size = input('what side do you want? S, M, L \n')
add_peperoni = input('Do you want peperoni? Y or N \n')
extra_cheese = input('Do you want extra cheese? Y or N \n')

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_peperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
else:
    bill == bill

if extra_cheese == 'Y':
    bill += 1
else:
    bill == bill

print(f'Your final bill is {bill}')

#using count and lower functions.
name = 'JOE HALIMAT OSHIMHEOWE'
name_read = name.lower()
t = name_read.count('e')
print(t)


#coding challange.
print('Welcome to my treasure island adventure!')
print('Make the right choices to survive the island and get your treasure!')

step_1 = input('You\'re at a cross road....Which way do you you want to go? Left or Right \n').lower()

if step_1 == 'left':
    step_2 = input('You\'re at a river....what do you want to do? to swim type "swim" or to wait for a boat type "wait"\n').lower()
    if step_2 == 'wait':
        step_3 = input('you have arrived at a house with 3 door.....which door do you want to go through? red or blue or green\n').lower()
        if step_3 == 'green':
            print('you found the treasure, YOU WIN!')
        elif step_3 == 'red':
            print('ohh no room full of lava1, GAME OVER!')
        elif step_3 == 'blue':
            print('ohh no a room crocodiles!, GAME OVER1')
        else:
            print('door those not exist, GAME OVER!')
    else:
        print('ohh no you drowned, GAME OVER!')
else:
    print('ohh no you fell into a pit, GAME OVER!')


