print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15.00

elif size == "M":
    bill = 20.00

elif size == "L":
    bill = 25.00

if add_pepperoni == "Y" and size == "S":
    bill += 2.00

elif add_pepperoni == "Y" and size == "L" or "M":
    bill += 3.00

if extra_cheese == "Y":
    bill += 1.00
    print(f"Your final bill is: ${bill:.2f}.")

else:
    print(f"Your final bill is: ${bill:.2f}.")
