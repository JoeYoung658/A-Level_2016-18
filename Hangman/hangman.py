#Hangman Game (v2.0) Name: Joe Young Date: 24/09/2016 minimin about of lines
#test
import sys
sys.path.append(sys.path[0]+'\\Extra')
from random import *
from time import *
import hangmanp
def random_word(filename): #Opens file, gets sets to word list and returns a random word
    file = open (filename) 
    word_list = file.readlines() 
    file.close()
    single_word = (word_list[randint(0, len(word_list)-1)]) 
    return single_word
def play_again():
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
    ran_word = random_word(sys.path[0]+'\\Extra\wordlists.txt')
    li = (len(ran_word)-1)
    left = ["_" for i in range (li)]
    trys = 0
    guess = 0
    print(ran_word)
    while 0 != 1:
        for place in left:
            print(place, end=" ")
        print ("\nThe Word has ", li, " letters! \nGuess = ", trys )
        letter = str(input("What is your guess?\n-")).lower()
        if ran_word.find(letter) == -1:
            print ("Your guess was incorrect\n")
            if guess != 11:
                print (hangmanp.hangman(guess))
                guess += 1
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

            if not(("_") in left): 
                for place in left:
                    print(place, end=" ")
                print("\nYou have won the game!, it took you ", trys, " guesses!\n")
                sleep(3)
                return play_again()
                break
        trys += 1
        if not(guess != 11):
                print("You have exceed your guesses!\n")
                print("You have lost the game!, it took you ", trys, "trys to fail :(\n")
                sleep(5)
                return play_again()
                break
if __name__ == "__main__":
    main()