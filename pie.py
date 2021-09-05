numbers = [9, 8, 7, 6, 5]

result =[]

def reverseArray(array):
    reverse = []
    for i in range(len(array), 0, -1):
        reverse.append(array[i -1])
    return reverse

for item in numbers:
    print(item)

result = reverseArray(numbers)

for item in result:
    print(item)

