for num in range(1, 101):
    string = ""
    if num  % 3 == 0:
        string += "Fizz"
    elif num % 5 == 0:
        string += "Buzz"
    elif num % 3 != 0 and num % 5 != 0:
        string += str(num)
    print(string)
