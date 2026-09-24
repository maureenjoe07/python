#BMI calculator
#get_weight = float(input("What is your weight?  "))
#get_height = float(input("What is your height?  "))

#BMI_cal = get_weight / (get_height**2)

#print(round(BMI_cal, 3))

def is_leap(year):
    if year % 4 == 0:
        if  year % 100 != 0 or year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("False")


year = int(input('Enter a year: '))
 
is_leap(year)