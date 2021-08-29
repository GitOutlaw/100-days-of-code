# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello John")
#     print("How do you do Peter")
#     print("Isn't the weather nice today?")


# greet()

# Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_with_name("John")

# greet_with_name("Tom")

# Functions with more than 1 input. Positional Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's the weather like in {location} ?")


# Keyword Arguments

greet_with(location="Texas", name="John" )