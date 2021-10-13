student_heights = input("Input a list of student heights: ").split()

# converts list input into int
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#  sums all items in list
total_height = 0

for height in student_heights:
    total_height += height

# counts number of items in list
number_of_students = 0

for student in student_heights:
    number_of_students += 1

# gives total to print
total = total_height / number_of_students

# prints rounded total
print(round(total))
