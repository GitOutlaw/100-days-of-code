print("Welcome to the rollercoaster!")
height = int(input("What's your height in inches: "))
bill = 0

if height >= 47:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age <= 12:
        bill = 5.00
        print("Child tickets are $5.00.")
    elif age <= 18:
        bill = 7.00
        print("Youth tickets are $7.00.")
    elif age >= 45 and age <= 55:
        bill = 0.00
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12.00
        print("Adult tickets are $12.00.")

    wants_photo = input("Do you want a photo? Y or N: ")
    if wants_photo == "Y":
        bill += 3.00
    print(f"Your final bill is ${bill:.2f}")

else:
    print("Sorry, you have to grow taller before you can ride.")
