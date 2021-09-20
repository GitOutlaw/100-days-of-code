# from coffee_machine_data import MENU, resources, coins

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. User input asking the menu
# TODO: 2. Turning off for maintenance
# TODO: 3. Check resources using report
# TODO: 4. Check enough resources to make coffee


def resource_check(drink, ingredient_type):
    ingredients_check = MENU[drink]['ingredients'][ingredient_type]
    resources_check = resources[ingredient_type]

    if ingredients_check <= resources_check:
        return True
    elif ingredients_check > resources_check:
        return False

def check(water_check, milk_check, coffee_check):

    if water_check:
        if milk_check:
            if coffee_check:
                print('Please insert coins.')
                return True
            else:
                print(f"Sorry there is not enough coffee.")
        else:
            print(f"Sorry there is not enough milk.")
    else:
        print(f"Sorry there is not enough water.")


# TODO: 5. Input coins by user

def money(name_of_coins):
    ask_money = int(input(f"how many {name_of_coins}?: "))
    return ask_money


# TODO: 6. Calculate transaction

def calculate_transaction(money_insufficient, give_change, same, change):
    if money_insufficient:
        print("Sorry that's not enough money. Money refunded.")
        continue_serving = False
    elif give_change:
        print(f"Here is ${change} dollars in change.")
        return True
    elif same:
        return True

# TODO: 7. Add profit before making coffee
# TODO: 8-1. Make coffee deduct ingredients

def ingredients_deduction(drink, ingredient_type):
    resources[ingredient_type] -= MENU[drink]['ingredients'][ingredient_type]

#TODO: 8-2.  Print serving
#TODO: 10. serve the next customer by repeating from todo1

def menu():
    user_choice = input(" What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        
        

    elif user_choice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
        

    elif user_choice == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        

    elif user_choice == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
    
# elif user_choice == "off":
    




