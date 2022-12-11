from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
"""On vas crée un objet """
mony_machine = MoneyMachine()
coffee_nake = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_nake.report()
        mony_machine.report()
    else:
        """comment verifier que nous avons suffisament de ressource"""
        drink = menu.find_drink(choice)
        if coffee_nake.is_resource_sufficient(drink) and mony_machine.make_payment(drink.cost):
           coffee_nake.make_coffee(drink)
