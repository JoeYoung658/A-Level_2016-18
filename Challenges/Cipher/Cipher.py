#cipher 
#sys.path[0]+'\\Extra\\Assembly.txt'

import sys



def convert_to_ascii(string):
    text = []
    for char in string:
        text.append(int(ord(char)))
    return text

def convert_to_word(ascii_list):
    text = ""
    for dec in ascii_list:
        text += chr(int(dec))
    return text

def increase_ascii(ascii_list, amount):
    # z is 122
    # Z is 90
    # a is 97
    # A is 65
    
    for i in range(len(ascii_list)):
        if ascii_list[i] == 122:
            ascii_list[i] = 97
            ascii_list[i] += amount -1
        elif ascii_list[i] == 90:
            ascii_list[i] = 65
            ascii_list[i] += amount -1
        else:
            ascii_list[i] += amount
    
    return ascii_list

def decrease_ascii(ascii_list, amount):
    for i in range(len(ascii_list)):
        ascii_list[i] -= amount
    return ascii_list




change_amount = int(input("How much would you like to change the cipher?\n>"))
print(change_amount)
print("--------------------------------")


# file_name = sys.path[0]+'\\Extra\Input.txt'
# with open(file_name) as myfile:
#     user_input="".join(line.rstrip() for line in myfile)

user_input = "AaBbZzyY"

print(user_input)

ascii_list = convert_to_ascii(user_input)
print(ascii_list)

Oringal_Sentace  = convert_to_word(ascii_list)
#print(Oringal_Sentace)

increased_ascii_list = increase_ascii(ascii_list, change_amount)
#print(increased_ascii_list)

cipher = convert_to_word(increased_ascii_list)
print(cipher)


decreased_ascii_list = decrease_ascii(increased_ascii_list, change_amount)
#print(decreased_ascii_list)

uncipher = convert_to_word(decreased_ascii_list)
#print(uncipher)


file_name = sys.path[0]+'\\Extra\Output.txt'
file = open(file_name, 'a')
file.write(cipher)
file.close



print("Done")









