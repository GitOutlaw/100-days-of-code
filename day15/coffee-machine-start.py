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

profit = 0


def is_resource_sufficient():
    """Returns True when order can be made, False if ingredients are insufficient."""
    return


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01

    print(f"")


    
    # change = total_coins - MENU["latte"]["cost"]

    return


def is_transaction_successful():
    """Return True when the payment is accepted, or False if money is insufficient."""
    return

def make_coffee():
    """Deduct the required ingredients from the resources."""
    return










# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])



# TODO: 1. User input asking the menu
# TODO: 2. Turning off for maintenance
# TODO: 3. Check resources using report
# TODO: 4. Check enough resources to make coffee


# TODO: 5. Input coins by user


# def check_coins(check):
#     coin_check = total_coins


# TODO: 6. Calculate transaction

# TODO: 7. Add profit before making coffee
# TODO: 8-1. Make coffee deduct ingredients


# TODO: 8-2.  Print serving
# TODO: 10. serve the next customer by repeating from todo1