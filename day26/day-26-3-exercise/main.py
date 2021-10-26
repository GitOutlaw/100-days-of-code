with open("day26/day-26-3-exercise/file1.txt", encoding="utf8") as file1:
    file_1_data = file1.readlines()

with open("day26/day-26-3-exercise/file2.txt", encoding="utf8") as file2:
    file_2_data = file2.readlines()


result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)
