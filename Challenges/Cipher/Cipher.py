#cipher 
#sys.path[0]+'\\Extra\\Assembly.txt'

import sys



def convert_to_ascii(string):
    text = []
    for char in string:
        text.append(str(ord(char)))
    return text

def convert_to_word(ascii_list):
    text = ""
    for dec in ascii_list:
        text += chr(int(dec))
    return text

def increase_ascii(ascii_list, amount):
    for i in range(len(ascii_list)):
        ascii_list[i] += amount
    return ascii_list

def decrease_ascii(ascii_list, amount):
    for i in range(len(ascii_list)):
        ascii_list[i] -= amount
    return ascii_list



user_input = "Hello my name is Joe!"

ascii_list = convert_to_ascii(user_input)

sentance  = convert_to_word(ascii_list)

increased_ascii_list = increase_ascii([int(i) for i in ascii_list], 1)

new_ascii_list = [str(i) for i in increased_ascii_list]

increased_sentance  = convert_to_word(new_ascii_list)

decrease_sentance = decrease_ascii(increased_ascii_list, 1)

new_sentance = convert_to_word(decrease_sentance)

print(ascii_list)
print(sentance)
print(increased_ascii_list)
print(new_ascii_list)
print(increased_sentance)
print(decrease_sentance)
print(new_sentance)







#print(ord(user_input))

##text = ""
##for i in range(len(user_input)):
##    text += chr(user_input[i])
##print(user_input)
