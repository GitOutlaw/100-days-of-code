from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates objects from classes.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Sets variable for while loop.
is_on = True

# While loop, uses is_on.
while is_on:
    # Creates object from Menu().
    option = menu.get_items()
    # User input option.
    choice = input(f"What would you like? ({option}) ")
    # Off funcion using is_on variable.
    if choice == "off":
        is_on = False
    # Report function uses CoffeeMaker and MoneyMachine report.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Creates object from Menu().
        drink = menu.find_drink(choice)
        # Creates object from CoffeeMaker().
        is_enough_resources = coffee_maker.is_resource_sufficient(drink)
        # Creates object from MoneyMachine().
        is_transaction_successful = money_machine.make_payment(drink.cost)
        # When condtions are True, object coffee_maker will make coffee.
        if is_enough_resources and is_transaction_successful:
            coffee_maker.make_coffee(drink)
