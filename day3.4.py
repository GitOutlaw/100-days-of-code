print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")

price = 0

if size == "S":
    price = 15.00

elif size == "M":
    price = 20.00

elif size == "L":
    price = 25.00

add_pepperoni = input("Do you want pepperoni? Y or N: ")

if add_pepperoni == "Y" and size == "S":
    price += 2.00
    print(f"Your final bill is: ${price:.2f}")
elif add_pepperoni == "Y" and size == "L" or "M":
    price += 3.00
    print(f"Your final bill is: ${price:.2f}")

add_extra_cheese = input("Do you want extra cheese/ Y or N: ")

if add_extra_cheese == "Y":
    price += 1.00
    print(f"Your final bill is: ${price:.2f}")

elif add_extra_cheese == 'Y' and  :
    price += 

