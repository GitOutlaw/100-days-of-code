# List Comprehension
# Keyword comprehension
# new list = [new_item for item in list]
# new_list = [letter for letter in name]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "John"
# letters_list = [letter for letter in name]
# print(letters_list)

# range_list = [num * 2 for num in range(1,5)]
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# test = [new_item for name in names if test]

# short_names = [name for name in names if len(name) < 5]
# print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)