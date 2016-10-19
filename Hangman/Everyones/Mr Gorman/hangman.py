""" Hangman Game (v1.0)
    Name: Mr Gorman
    Date: 22/09/2016
    """

import os
import random

def random_word(filename):
    word_list = []

    with open(filename, "r") as file:
        for line in file:
            line = line.replace("\n", "").upper()
            word_list.append(line)

    index = random.randint(0, len(word_list) - 1)
    word = word_list[index]
    return word

def find_character(char, word):
    char_indices = []
    index = 0
    for character in word:
        if character == char:
            char_indices.append(index)
        index += 1

    return char_indices

def create_placeholders(word):
    placeholders = ["_" for i in range(len(word))]
    spaces = find_character(" ", word)
    n_spaces = len(spaces)

    if n_spaces > 0:
        for index in spaces:
            placeholders[index] = " "
    
    return placeholders, n_spaces

def display_info(placeholders, letters_remaining, attempts_remaining):
    print()
    for place in placeholders:
        print(place, end=" ")
    print("\n\nLetters remaining = %d, Attempts remaining = %d\n" % (letters_remaining, attempts_remaining))

def main():
    VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filename = os.path.dirname(__file__) + "\word_list.txt" # os.path.dirname() required if running outside of the script directory
    #word_list = load_file(filename)
    game_over = False

    while not game_over:
        filename = os.path.dirname(__file__) + "\word_list.txt"
        word = random_word(filename)
        placeholders, n_spaces = create_placeholders(word)
        n_chars = len(word)
        letters_remaining = n_chars - n_spaces
        attempts_remaining = 10
        letters_guessed = []
        turn_over = False

        while not turn_over:

            display_info(placeholders, letters_remaining, attempts_remaining)

            valid_input = False
            while not valid_input:        
                char = input("Enter a letter: ").upper()
                if len(char) == 1 and VALID_CHARS.find(char) != -1:
                    valid_input = True
                else:
                    print("Invalid input!")

            char_indices = find_character(char, word)
            n_chars_found = len(char_indices)

            if letters_guessed.count(char) == 0:
                if n_chars_found > 0:
                    for index in char_indices:
                        placeholders[index] = char
                    letters_guessed.append(char)
                    letters_remaining -= n_chars_found
                    print("That's right!")
                else:
                    letters_guessed.append(char)
                    attempts_remaining -= 1
                    print("That's wrong!")
            else:
                print("You already guessed that letter!")
            
            if attempts_remaining == 0:
                print("YOU LOSE!")
                turn_over = True
            elif letters_remaining == 0:
                print("YOU WIN!")
                turn_over = True

        print("The word was: %s" % word)
        
        valid_input = False
        while not valid_input:
            player_input = input("\nDo you want to play again (y/n)? ").lower()
            if player_input == "y":
                valid_input = True
            elif player_input == "n":
                valid_input = True
                game_over = True


if __name__ == "__main__":
    main()
