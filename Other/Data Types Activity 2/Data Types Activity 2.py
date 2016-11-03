"""
Joe Young
Activity Types Activity 2
#V.1
"""
first_name = input("What is your first name?").lower()
last_name = input("What is your last name?").lower()
gender = input("Are you M or F?").lower()
test_mark_1 = int(input("What was the first test mark?"))
test_mark_2 = int(input("What was the second test mark?"))
test_mark_3 = int(input("What was the last test mark?"))
average = (test_mark_1 + test_mark_2 + test_mark_3)
average = average/3
print("The average test mark is,", average)