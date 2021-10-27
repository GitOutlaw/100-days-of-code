# Dictionary Comprehension

import random

# new_dict = {new_key: new_value for item in list}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Conditional Dictionary Comprehension
# another_dict = {new_key: new_value for (key, value) in dict.items()}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
