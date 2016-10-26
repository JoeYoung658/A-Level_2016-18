""" Hangman Game (v1.0)
    Name: samuel armstrong
    Date: 
    """

import random
count=0

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
    return word

def find_character(char, word,):
    global count
    """ Function to return the position(s) of a character in word;
        Note: This should return the index of the character as an integer,
        if the character is not found, it should return a value of -1
        """

    
    index = 0
    while index < len(word):
        index = word.find(char, index)
        if index == -1:
            print ("letter not found within the word")
            break
        index = index + 1
        print('your charcter was found at position: ', index)
        count = count + 1

##        cant append to list correctly
##        indices=[]

##        indices.append(word.find(char, index))
   



def main():
    global count
    """ Note: This is your main function and should contain your game loop.
        """
    i= input ("would you like to play a game y/n: ").lower()
    while i== "y":
        fudge = "word_list.txt"
        attempts_remaining = 10
        word_list = load_file("word_list.txt")
        word = select_word (word_list)
        print ("the word is" , len(word), " letters long")
        while  attempts_remaining !=0:
            char = input ("letter: ")   
            char_pos = find_character (char, word,)
            attempts_remaining = attempts_remaining -1
            print ("attempts remaining: ",attempts_remaining)
            if count == len(word):
                print ("well done you have got all the letter the word was",word)
                i= input ("would you like to play a game y/n: ").lower()
                break
            
            
    print ("game over")
if __name__ == "__main__":
    main()
