#Data types, number operations, type conversions, f-string.

two_digit_number = input('enter a two digit number\n')

a = two_digit_number[0]
b = two_digit_number[1]

c = int(a) + int(b)

print(c)

weight = int(input('enter your weight (kg)\n'))
height = float(input('enteer ypur height (m)\n'))

BMI = int(weight / height**2)

print(BMI)

#f-strings
score = 3
height = 1.8
isWinning = True

print(f'your score is {score}, your height is {height},you are winning this {isWinning}')

age = int(input('enter your age.\n'))
total_life_span = 4_320        # in weeks
age_in_weeeks = age * 48

time_left = total_life_span - age_in_weeeks

print(f'You have {time_left} weeks left')