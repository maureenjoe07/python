#OBJECT ORIENTED PROGRAMMING.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#genarated and object from the class.
coffee_maker = CoffeeMaker()    
money_machine = MoneyMachine()   
menu = Menu()       
# menu_item = MenuItem()           

#Applying the methods and attributes under the classes.
# coffee_maker.report()        
# money_machine.report()      
on = True
while on == True:
    order = input(f'what would you like to get?({menu.get_items()}) ')
    if order == 'report':
        coffee_maker.report()        
        money_machine.report() 
    elif order == 'off':
        on = False
        print('Machine off.')
        # break
    else:
        drink = menu.find_drink(order)
        condition = coffee_maker.is_resource_sufficient(drink)
        if condition == True:
            cash = money_machine.make_payment(condition)
            if cash == True:
                coffee_maker.make_coffee(drink)
        
            




