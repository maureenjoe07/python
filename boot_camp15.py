# COFFEE DEPENSER.
#resources library(tell me what i have in the manchine - 1000ml water, 200ml milk, 100gcoffee)
resources = {
    'Water(ml)': 1000,
    'Milk(ml)': 200,
    'coffee(g)': 100,
    'Money($)': 0,
}

#library of each drink and it's ingredents
drinks = {
    'Espresso': {
        'Ingredents': {
            'Water(ml)': 50,
            'coffee(g)': 18,
        },
        'Cost($)': 1.50
    },
    'Latte': {
        'Ingredents': {
            'Water(ml)': 500,
            'Milk(ml)': 150,
            'coffee(g)': 24,
        },
        'Cost($)': 2.50
    },
    'Cappuccino': {
        'Ingredents': {
            'Water(ml)': 250,
            'Milk(ml)': 100,
            'coffee(g)': 24,
        },
        'Cost($)': 3.00
    }
    }

# modify the resources list
def modify_resources():
    if order == 'Espresso' and  make_coffee == True:
        resources['Money($)'] += drinks['Espresso']['Cost($)']
        resources['Water(ml)'] -= drinks['Espresso']['Ingredents']['Water(ml)']
        resources['coffee(g)'] -= drinks['Espresso']['Ingredents']['coffee(g)']
    elif order == 'Latte' and  make_coffee == True:
        resources['Money($)'] +=  drinks['Latte']['Cost($)']
        resources['Water(ml)'] -= drinks['Latte']['Ingredents']['Water(ml)']
        resources['coffee(g)'] -= drinks['Latte']['Ingredents']['coffee(g)']
        resources['Milk(ml)'] -= drinks['Latte']['Ingredents']['Milk(ml)']
    elif order == 'Cappucino' and  make_coffee == True:
        resources['Money($)'] = drinks['Cappuccino']['Cost($)']
        resources['Water(ml)'] -= drinks['Cappuccino']['Ingredents']['Water(ml)']
        resources['coffee(g)'] -= drinks['Cappuccino']['Ingredents']['coffee(g)']
        resources['Milk(ml)'] -= drinks['Cappuccino']['Ingredents']['Milk(ml)']

on = True
while on == True:
    #ask what i want to drink(espresso, latte, cappuccino)
    order = input('What will you like (Espresso, Latte, Cappuccino): ').title()

    #to check resources
    if order =='Resources'.title():
        for key in resources:
            print(f'{key}: { resources[key]}')
        # order = input('What will you like (Espresso, Latte, Cappuccino): ').title()
    elif  order == 'Off'.title():                #turn off machine
        on = False
        print('Machine off.')
        break

    #ask how many coins i have accordimg to name
    print('Pls insert coins.')
    num_pen = int(input('How many penny: '))
    num_nic = int(input('How many nickle: '))
    num_dime = int(input('How many dime: '))
    num_quar = int(input('How many quarter: '))

    #doing the maths for the coins(1P-1C(0.01), 1N-5C(0.05), 1D-10C(0.10), 1Q-25C(0.25))
    cash_input = 0

    amt_pen = num_pen * 0.01
    amt_nic = num_nic * 0.05 
    amt_dime = num_dime * 0.10
    amt_quar = num_quar * 0.25
    total = amt_pen + amt_nic + amt_dime + amt_quar

    cash_input += total

    #check if coin is enoung and also return change if any
    if order == 'Espresso':
        amt_espresso = drinks['Espresso']['Cost($)']
        if amt_espresso <= cash_input and amt_espresso:
            if drinks['Espresso']['Ingredents']['Water(ml)'] <= resources['Water(ml)']:
                if drinks['Espresso']['Ingredents']['coffee(g)'] <= resources['coffee(g)']:
                    change = round((cash_input - amt_espresso), 2)
                    print(f'Here is ${change} in change.')
                    make_coffee = True
                    print('Here is your coffee. Enjoy!')
                else:
                    make_coffee = False
                    print('Sorry not enough coffee, Money refund.')
            else:
                make_coffee = False
                print('Sorry not enough water, Money refund.')
        else:
            make_coffee = False
            print("Sorry that's not enough money, Money refund.")
    elif order == 'Latte':
        amt_latte = drinks['Latte']['Cost($)']
        if amt_latte <= cash_input:
            if drinks['Latte']['Ingredents']['Water(ml)'] <= resources['Water(ml)']:
                if drinks['Latte']['Ingredents']['coffee(g)'] <= resources['coffee(g)']:
                    if drinks['Latte']['Ingredents']['Milk(ml)'] <= resources['Milk(ml)']:
                        change = round((cash_input - amt_latte), 2)
                        print(f'Here is ${change} in change.')
                        print('Here is your coffee. Enjoy!')
                    else:
                        make_coffee = False
                        print('Sorry not enough milk, Money refund.')
                else:
                    make_coffee = False
                    print('Sorry not enough coffee, Money refund.')
            else:
                make_coffee = False
                print('Sorry not enough water, Money refund.')
        else:
            make_coffee = False
            print("Sorry that's not enough money. Money refund.")
    elif order == 'Cappuccino':
        amt_cappuccino = drinks['Cappuccino']['Cost($)']
        if amt_cappuccino <= cash_input:
            if drinks['Cappuccino']['Ingredents']['Water(ml)'] <= resources['Water(ml)']:
                if drinks['Cappuccino']['Ingredents']['coffee(g)'] <= resources['coffee(g)']:
                    if drinks['Cappuccino']['Ingredents']['Milk(ml)'] <= resources['Milk(ml)']:
                        change = round((cash_input - amt_cappuccino), 2)
                        print(f'Here is ${change} in change.')
                        print('Here is your coffee. Enjoy!')
                    else:
                        make_coffee = False
                        print('Sorry not enough milk, Money refund.')
                else: 
                    make_coffee = Falsemake_coffee = False
                    print('Sorry not enough coffee, Money refund.')
            else:
                make_coffee = False
                print('Sorry not enough water, Money refund.')
        else:
            make_coffee = False
            print("Sorry that's not enough money. Money refund.")
            
        # modify the resources list
    modify_resources()
    
    

