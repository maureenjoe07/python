#for loop, range and code blocks.
fruits = ['apple', 'mango', 'pear']
for fruit in fruits:
    print(fruit)
    print(fruit + ' juice')


student_heights = input('enter your heights. ').split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
total_height = 0                        # in place of sum function.
for height in student_heights:
    total_height += height
    
print(total_height)

number_of_students = 0                  # in place of len function.
for student in student_heights:
    number_of_students += 1

print(number_of_students)

average_height = total_height // number_of_students
print(average_height)


    
student_scores = input('enter the list of scores').split( )
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
highest_score = 0                         # in place of min and max function.
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f'The highest score in the class is: {highest_score}')


for number in range (1, 10, 2):
    print(number)

total = 0
for number in range (1,101):
    total += number

print(total)

#printing all even numbers between a range of numbers.
target = int(input('enter a target value\n'))
for number in range (2, target + 1, 2):
    print(number)

#fizz buzz (divisibility by 3 and 5).
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('fizz buzz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0:
        print('fizz')
    else:
        print(number)
   
#password generator project.
import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers= ['0','1','2','3','4','5','6','7','8','9',]
symbols = ['*','(',')','[',']','/','$','_','-','&','@']

print('Welcome to the pypassword generator!')
num_letters = int(input('How many letters do you want?\n'))
num_numbers = int(input('How many numbers do you want?\n'))
num_symbols = int(input('How many symbols do you want?\n'))
 
result_1 = ''
for i in range(num_letters):
    num_letters = str(num_letters)
    category_1 = random.randint(0, len(letters) - 1)
    result_1 += letters[category_1]

result_2 = ''
for j in range(num_numbers):
    num_numbers = str(num_numbers)
    category_2 = random.randint(0, len(numbers) - 1)
    result_2 += numbers[category_2]

result_3 = ''
for k in range(num_symbols):
    num_symbols = str(num_symbols)
    category_3 = random.randint(0, len(symbols) - 1)
    result_3 += symbols[category_3]

password = result_1 + result_2 + result_3

password_list = []
for value in password:
    password_list += value

random.shuffle(password_list)

final_password = '' 
for char in password_list:
    final_password += char
print (f'your passwors is: {final_password}')