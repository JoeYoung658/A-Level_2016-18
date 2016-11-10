#cipher 
#sys.path[0]+'\\Extra\\Assembly.txt'

import sys



def convert_to_ascii(string):
    text = []
    for char in string:
        text.append(str(ord(char)))
    return text


    #return " ".join(str(ord(char)) for char in string)

def convert_to_word(ascii_list):
    text = ""
    for dec in ascii_list:
        text += chr(int(dec))
    return text

def 


user_input = "Hello my name is Joe"

ascii_list = convert_to_ascii(user_input)
sentance  = convert_to_word(ascii_list)

print(ascii_list)
print(sentance)





#print(ord(user_input))

##text = ""
##for i in range(len(user_input)):
##    text += chr(user_input[i])
##print(user_input)
