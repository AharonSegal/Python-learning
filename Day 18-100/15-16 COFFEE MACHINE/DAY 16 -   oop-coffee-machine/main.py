from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    start = input(f"What would you like? {options}: ")
    if start == "off":
        is_on = False
    elif start == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        choice = menu.find_drink(start)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)

