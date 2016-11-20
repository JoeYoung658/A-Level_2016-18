"""
Cipher
Joe Young
V.2
"""

import sys
import random
def convert_to_ascii(string):
    """
    Takes a string and turns each character into decimal ascii
    """
    text = []
    for char in string:
        text.append(int(ord(char)))
    return text

def convert_to_word(ascii_list):
    """
    Takes a list of ascii and convets back into a string
    """
    text = ""
    for dec in ascii_list:
        text += chr(int(dec))
    return text

def increase_ascii(ascii_list, amount):
    """
    Inceases an ascii list, by amount set by user
    """
    # z is 122
    # Z is 90
    # a is 97
    # A is 65
    for asci in range(len(ascii_list)):
        for i in range(amount):
            if ascii_list[asci] == 122:
                ascii_list[asci] = 97
                ascii_list[asci] += 1
            elif ascii_list[asci] == 90:
                ascii_list[asci] = 65
                ascii_list[asci] += 1
            else:
                ascii_list[asci] += 1
    return ascii_list

def decrease_ascii(ascii_list, amount):
    """
    Decreases an ascii list, by amount set by user
    """
    for asci in range(len(ascii_list)):
        for i in range(amount):
            if ascii_list[asci] == 97:
                ascii_list[asci] = 122
                ascii_list[asci] -= 1
            elif ascii_list[asci] == 65:
                ascii_list[asci] = 90
                ascii_list[asci] -= 1
            else:
                ascii_list[asci] -= 1
    return ascii_list

def main():
    file_name = sys.path[0]+'//Extra/Data.txt'
    with open(file_name) as myfile:
        user_input="".join(line.rstrip() for line in myfile)
    loop = True
    while loop:
        try:
            change_direction = int(input("Cipher- 1 Uncipher - 2\n>"))
            passwd = str(input("What is your password?\n-"))
            change_amount = random.Random(passwd).randint(0, 1000)
            
            print("--------------------------------")
            if change_direction == 1:
                ascii_list = convert_to_ascii(user_input)
                increased_ascii_list = increase_ascii(ascii_list, change_amount)
                cipher = convert_to_word(increased_ascii_list)
                loop = False
            elif change_direction == 2:
                ascii_list = convert_to_ascii(user_input)
                decreased_ascii_list = decrease_ascii(ascii_list, change_amount)
                cipher = convert_to_word(decreased_ascii_list)
                loop = False
            else:
                print("Unexpected input, please try again!")
        except NameError:
            print("Unexpected input, please try again!")
    open(file_name,"w").close()
    with open(file_name, 'w') as file_:
        file_.write(cipher)
    print("Written to file!")
    
if __name__ == "__main__":
    main()