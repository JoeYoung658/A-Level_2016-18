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
    for i in range(len(ascii_list)):
        ascii_list[i] += amount
    return ascii_list

def decrease_ascii(ascii_list, amount):
    for i in range(len(ascii_list)):
        ascii_list[i] -= amount
    return ascii_list


import random
passwd  = "Wat"
n = 1
file_name = sys.path[0]+'\\Extra\Data.txt'
#ran = random.Random(passwd).sample(range(1000), n)
ran = random.Random(passwd).randint(0, 1000)
print(ran)

print("--------------------------------")

#user_input = "Hello my name is Joe!"
# file = open(sys.path[0]+'\\Extra\Input.txt', 'r')
# user_input = file.read()
# file.close
with open(file_name) as myfile:
    user_input="".join(line.rstrip() for line in myfile)
open(sys.path[0]+'\\Extra\Data.txt',"w").close()

print(user_input)

# ascii_list = convert_to_ascii(user_input)
# print(ascii_list)

# Oringal_Sentace  = convert_to_word(ascii_list)
# print(Oringal_Sentace)

# increased_ascii_list = increase_ascii(ascii_list, ran)
# print(increased_ascii_list)

# cipher = convert_to_word(increased_ascii_list)
# print(str(cipher))


# decreased_ascii_list = decrease_ascii(increased_ascii_list, ran)
# print(decreased_ascii_list)

# uncipher = convert_to_word(decreased_ascii_list)
# print(uncipher)


# file = open(file_name, 'a')
# file.write()
# file.close


"""
---------------
uncipher from file
"""

ascii_list = convert_to_ascii(user_input)
#print(ascii_list)

decreased_ascii_list = decrease_ascii(ascii_list, ran)
#print(decreased_ascii_list)

uncipher = convert_to_word(decreased_ascii_list)
print(uncipher)



# with open(fname + '.new', 'w',
#           encoding="ascii", errors="surrogateescape") as f:
#     f.write(cipher)


print("Done")









#increased_ascii_list = increase_ascii([int(i) for i in ascii_list], ran)
#string_ascii_list = [str(i) for i in increased_ascii_list]
#print(string_ascii_list)
#print(ord(user_input))

##text = ""
##for i in range(len(user_input)):
##    text += chr(user_input[i])
##print(user_input)


# cipher2 = str(cipher.encode('utf-8').strip())
# # print(cipher2)

# ascii_list2 = convert_to_ascii(cipher2)
# # print (ascii_list2, "2")

# uncipher2 = convert_to_word(ascii_list2)
# print(uncipher2)