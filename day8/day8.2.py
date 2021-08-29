#Write your code below this line 👇

def prime_checker(number):
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)








# def prime():
    num = int(input("Enter a number: "))

    # If given number is greater than 1
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(f"{num}, is a prime number")

    else:
        print(f"{num}, is not a prime number")

# prime()
