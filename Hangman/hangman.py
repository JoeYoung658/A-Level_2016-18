""" Hangman Game (v1.0)
    Name: Joe Young
    Date: 24/09/2016
    """

#Joe Young
#06/09/2016
import sys
import platform
if "windows" == platform.system():
    sys.path.append(sys.path[0]+'\\Extra')
else:
    sys.path.append(sys.path[0]+'//Extra')
from random import *
from time import *
import hangmanp
def load_file(filename):#Opens file and returns a full list of words
    file = open (filename) 
    word_list = file.readlines() 
    file.close() 
    return word_list 

def select_word(): #gets single random word from list
    word_list = load_file("wordlists.txt") 
    single_word = (word_list[randint(0, len(word_list)-1)]) 
    return single_word 

def again():
    while 0 != 1:
        again = str(input("Would you like to play again?\n-")).lower()
        if again == "yes":
            print("You have choosen to play again!\n")
            sleep(1)
            return main()
        elif again == "no":
            print("You have choosen to not play again!")
            sleep(3)
            break
        else:
            print("Please input a vaild method!\n")

def main():
    ran_word = select_word()
    li = (len(ran_word)-1)
    trys = 0
    guess = 0
    print(ran_word)
    left = ["_" for i in range (li)]
    while 0 != 1:
        print (left)
        letter = str(input("What is your guess?\n-")).lower()
        if ran_word.find(letter) == -1:
            print ("Your guess was incorrect\n")
            if guess != 11:
                print (hangmanp.hangman(guess))
                guess = guess + 1
        else:
            if not(len(letter) == 1):
                print("Please only entre one letter at a time!\n")
            else:
                if not((letter) in left):
                    print("Your guess was correct!\n")
                else:
                    print("You have already correctly guessed", letter, "!\n")
            
            for i in range(li):
                if ran_word[i] == letter:
                    left[i] = letter

            if not(("_") in left): #checks to see if user has won the game
                print(left)
                print("You have won the game!, it took you ", trys, " guesses!\n")
                sleep(3)
                return again()
                break
        trys = trys + 1
        if not(guess != 11):
                print("You have exceed your guesses!\n")
                print("You have lost the game!, it took you ", trys, " to fail :(\n")
                sleep(5)
                return again()
                break

                
if __name__ == "__main__":
    main()






