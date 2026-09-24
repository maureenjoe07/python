from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

class Coffee_shop:
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()
    def __int__(self):
        # self.menu = Menu()
        pass

    def place_order(self,drink):
        # drink = input('What will you like (Espresso, Latte, Cappuccino):').lower()
        item = self.menu.find_drink(drink)
        # print(drink)
        if not item:
            print(self.menu.get_items())
            return 
            # drink = input('What will you like (Espresso, Latte, Cappuccino):').lower()
        # cost = item.cost
        # self.moneyMachine.process_coins()
        make = self.coffeeMaker.is_resource_sufficient(item)
        if not make:
            return
        proceede = self.moneyMachine.make_payment(item.cost)
        if not proceede:
            return
        self.coffeeMaker.make_coffee(item)

    def fetch_report(self):
        self.coffeeMaker.report()
       
    def gain(self):
        print(self.moneyMachine.profit)

# on = True
# while on == True:
#     v1 = Coffee_shop()
#     v1.place_order()


v1 = Coffee_shop()
on = True
while on == True:
    process = input('What will you like (Espresso, Latte, Cappuccino):' ).lower()
    if process == "report":
        v1.fetch_report()
    elif process == 'off'.lower():
        on = False
        # break
    elif process == 'profit'.lower():
        v1.gain()
    else:
        v1.place_order(process)