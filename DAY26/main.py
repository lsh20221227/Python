# List comprehension

# new_list = [new_item for item in list]
# number = [1,2,3]
# new_list = [n+1 for n in number]
# print(new_list)
#
# name = "Angela"
# new_list2 = [letter for letter in name]
# print(new_list2)
#
# ranges = range(1,5)
# new_list3 = [n*2 for n in ranges]
# print(new_list3)
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


#---------------------------------------------------------------------------------------------------------------------

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# # squared_numbers = [number*number for number in numbers]
# squared_numbers = [number**2 for number in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)

#--------------------------------------------------------------------------------------------------------------

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [n for n in numbers if n%2==0]
#
#
# #Write your code 👆 above:
#
# print(result)

#--------------------------------------------------------------------------------------------------------------


# with open("file1.txt") as data1:
#      data = data1.readlines()
#
# with open("file2.txt") as data2:
#     data2 = data2.readlines()
#
# result = [int(d) for d in data if d in data2]
# print(result)


# if answer_state == "Exit":
#     missing_states = []
#     for state in all_states:
#         if state not in answer:
#             missing_states.append(state)
#     new_data = pandas.DataFrame(missing_states)
#     new_data.to_csv("state_to_learn.csv")
#     break

# 이전에 한 us_states_game_start List Comprehension을 활용해서 다시 짜기
# if answer_state == "Exit":
#     missing_states = [state for state in all_states if state not in answer]
#     new_data = pandas.DataFrame(missing_states)
#     new_data.to_csv("states_to_learn.csv")
#     break

#------------------------------------------------------------------------

# names =['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
#
# students_scores = {student:random.randint(1, 100) for student in names}
#
# passed_students = {
#     key: value for (key ,value)  in students_scores.items()
#     if value > 60
# }
# print(passed_students)

#------------------------------------------------------------------------
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# example = [n for n in sentence.split()]
# result = { key:len(key)  for key in example}
#
# print(result)

#------------------------------------------------------------------------
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# weather_f = { key : value*9/5 +32 for key, value in weather_c.items()}
# # Write your code 👇 below:
# print(weather_f)

#------------------------------------------------------------------------



student_dict = {
    "student" : ["Angela" , "James", "Lily"],
    "score" : [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
#
# ['Angela', 'James', 'Lily']
# [56, 76, 98]

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98


# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64


# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#   print(row.student)

# Angela
# James
# Lily

# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)
# 56





















