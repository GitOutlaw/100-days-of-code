student_dict = {
    "student": ["John", "Angela", "Lily"],
    "score": [56,76,98]
}

# Loop in through dictionaries
# for (key, value) in student_dict.items():
#     print(value)


import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Loop through a data frame 
# for key, value in student_dataframe.items():
#     print(value)

# Loop through rows of a data frame (panda series) row.student
# for (index, row) in student_dataframe.iterrows():
    # if row.student == "Angela":
    # print(row.score)


# {new_key:new_value for (index, row) in df.items()}