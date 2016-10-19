#variables
filename = "word_list.txt"
word_list = []
screen_word = []
loop = 0
loop2= 0
play = "yes"
import random

#calling list
with open(filename, "r") as file:                                       
    for line in file:                                                   
        word_list.append(line.replace("\n", "").lower())                
                                                                        
print(word_list)
listlen = (len(word_list))
print (listlen)
while play == "yes":
    loop = 0
    loop2 = 0
    #choosing word
    wordnum = random.randint(0, (listlen - 1))
    print (wordnum)
    word = word_list[wordnum]
    print (word)

    wordlen = len(word)
    print (wordlen)

    #showing user blank word
    while loop != wordlen:
        screen_word.append("_")
        loop = loop + 1
    print (screen_word)

    #guess word

    while loop2 != 10:
        guess = input("Guess a letter:")
        char_indices = []
        for character in word:
            if character == guess:
                index = 0
                print ("filler")
                char_indices.append(index)
        #if (guess) is in (word):
            #add letter
                print ("yay")
                #a = word.index(guess)
##                screen_word.append(replace([char_indicies] (guess)))

        for index in char_indices:
            screen_word[index] = guess
            print (screen_word)

                
##        if word == ("full"):
##            print ("You Win!")
##            loop2 = 10
##            
##        else:
##            loop2 = loop2 + 1
        
    else:
        print ("Game Over")
        play = input("Would you like to play again? :")
            
