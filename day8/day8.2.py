# Write your code below this line 👇

def prime_checker(number="n"):
    # If given number is greater than 1
    if n > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(n/2)+1):
            # If num is / by any number between 2 and n / 2, it is not prime
            if (n % i) == 0:
                print("It's a prime number.")
                break
        else:
            print(f"It's not a prime number.")

    else:
        print(f"It's not a prime number.")

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))

prime_checker(number=n)
