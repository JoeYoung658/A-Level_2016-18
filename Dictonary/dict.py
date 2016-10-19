#Joe Young 17/10/2016
from time import sleep

my_dict = {"A" : "You selected A",
            "B" : "You selected B",
            "Default" : "Unrecongnised selection"}


user_input = input("What is your input? (A or B)").upper()

try:
    print(my_dict[user_input])
except KeyError:
    print(my_dict['Default'])

"""
if user_input not in my_dict:
    print(my_dict['Default'])
else:
    print(my_dict[user_input])
"""


sleep(3)
