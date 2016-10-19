#hangman
#16/09/2016
#create a file with large assortment of words in it and make computer append file and bring it back into an array

import random

def load_file(filename):
    word_list = []
    with open(filename, "r") as file:                                       
        for line in file:                                                   
            word_list.append(line.replace("\n", "").lower())                
    return word_list                                                                   

def select_word(word_list):

    randword = random.randint(0, len(word_list)-1)
    selected_word = word_list[randword]

    return selected_word

def find_character(guess, word):

    indices = []

    start = -1
    for i in range(len(word)):

        start = word.find(guess, start + 1)
        if start == -1:
            break
        indices.append(start)

    return indices


def main():
    foundletters = ""
    word_list = load_file("word_list.txt")
    word = select_word(word_list)
    neededletters = ["_" for i in range(len(word))]

    
    print ("welcome to hangman good luck guessing the word", word)
    print(neededletters)

    while 1 != 0:

        guess = str(input("What is your guess?")).lower()
        indicess = (find_character(guess, word))
        runtime = len(indicess)-1
        while runtime != -1:
            neededletters[indicess[runtime]] = guess
            runtime -= 1
            
        print(neededletters)
        print(indicess)



if __name__ =="__main__":
    main()

