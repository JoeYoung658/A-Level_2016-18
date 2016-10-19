##----------------------------------------------------
##  _    _                                           |
## | |  | |                                          |
## | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __    |
## |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   |
## | |  | | (_| | | | | (_| | | | | | | (_| | | | |  |
## |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  |
##                      __/ |                        |
##                     |___/                         |
##----------------------------------------------------
##          Hussain Salam | V0.1 | 22/09/2016        |
##----------------------------------------------------
##Imported Modules:
import random
##-----------------

def load_file(filename):
    """ Function to return a word list from a plain text file;
        Note: You will need to open the file, read and append
        each line to an array (or list), close the file and
        then return the array.
        """
    word_list = []

    with open(filename, "r") as file:                                        
        for line in file:                                           
            word_list.append(line.replace("\n", "").lower())                 
    return word_list




def select_word(word_list):
    """ Function to return a random word from an array of words;
        Note: You will need to import the random module and use
        random.randint() to select a random index in the array.
        """
    rand = random.randint(0, len(word_list)-1)
    word = (word_list[rand])
    print ("[DEBUG]:  Random word selected is:",word)
    
    return word
def find_character(word):
    """ Function to return the position(s) of a character in word;
        Note: This should return the index of the character as an integer,
        if the character is not found, it should return a value of -1
        """
    if attempts_remaining != 0:
        inc_char = []
        length = len(word)
        print ("[DEBUG]: The word length is",length)
        #length = length-1
        #print ("[DEBUG]: The NEW word length is",length)
        i=0
        while i != length:
            if char == word[i]:
                print("[SYSTEM]: The letter ",char,"' is correct. ")
                i=i+1
            else:
                i=i+1
                print("[SYSTEM]: Sorry, the letter '",char,"'is not correct. Try again!")
                inc_char.append([char])
                print (inc_char)
                
    else:
        print("btec")
    #return char_pos

# do you need any other functions or procedures?

def main():
    """ Note: This is your main function and should contain your game loop.
        """
    filename = "word_list.txt"
    attempts_remaining = 10
    global attempts_remaining
    
    # do you need any other variables?

    word_list = load_file("word_list.txt")
    print("[DEBUG]: Word list loaded: \n",word_list)
    word = select_word(word_list)
    char = input("[SYSTEM]: Please enter a character: ")
    char = find_character(word)
    global char
    # your code goes here

if __name__ == "__main__":
    main()
