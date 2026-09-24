#FUNCTIONS WITH OUTPUT.
def name_output(f_name, l_name):
    print(f_name.title()+' '+ l_name.title())

name_output(f_name= 'HALIMAT', l_name= 'JOE')

#CHALLANGE.
def is_leap(year):
    if year % 4 == 0:
        if  year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False 
    else:
        return False 

def days_of_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year)== True:
        if month == 2:
            print(F"This mobth has {month_days[month] + 1} days.")
        else:
            print(f'This month has {month_days[month]} days.')
    else:
        print(f'This month has  {month_days[month]} days.')

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))

is_leap(year)
print(is_leap(year))
days = days_of_month(year= year, month= month)

#CHALLANGE 2.
logo = r"""
 _____________________
|  _________________  |
| | JO           0. | |   _____      _      
| |_________________| |  / ____|    | |     
|  ___ ___ ___   ___  | | |     __ _| | ___ 
| | 7 | 8 | 9 | | + | | | |    / _` | |/ __|
| |___|___|___| |___| | | |___| (_| | | (__ 
| | 4 | 5 | 6 | | - | |  \_____\__,_|_|\___|
| |___|___|___| |___| |                     
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(logo)
num_1 = float(input('Enter a number: '))

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

operators = {
   '+' : add,
   '-' : subtract,
   '*' : multiply,
   '/' : divide,
}

for key in operators:
    print(key)

decision = input('Choose an opearator: ')

num_2 = float(input('Enter another number: '))

cal = operators[decision]
answer = cal(num_1, num_2)
print(answer)

end_cal = False
while end_cal == False:
    if input(f'enter "y" if you want to keep calculating with your previous answer({answer}) and "n" if not: ').lower() == 'y':
        num_1 = float(answer)
        decision = input('Choose an opearator: ')
        num_2 = float(input('Enter another number: '))
        cal = operators[decision]
        answer = cal(num_1, num_2)
        print(answer)
    else:
        end_cal = True

start_fresh = True
while start_fresh == True:
    if  input('Do you want to start a new calculation? - "y" or "n":  ') == 'y':
        num_1 = float(input('Enter a number: '))
        decision = input('Choose an opearator: ')
        num_2 = float(input('Enter another number: '))
        cal = operators[decision]
        answer = cal(num_1, num_2)
        print(answer)
        end_cal = False
        while end_cal == False:
            if input(f'enter "y" if you want to keep calculating with your previous answer({answer}) and "n" if not: ').lower() == 'y':
                num_1 = float(answer)
                decision = input('Choose an opearator: ')
                num_2 = float(input('Enter another number: '))
                cal = operators[decision]
                answer = cal(num_1, num_2)
                print(answer)
            else:
                end_cal = True
    else:
        start_fresh = False
        print('Goodbye')