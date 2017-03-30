#Joseph Young
import random # imports random
score = 0#sets score counter to 0
highscore = [0, 0 ,0]




print ("-------------------------Primary School quiz------------------------------------\n--------------------------------------------------------------------------------\n\n")
print ("Instrucations.\n You will be asked ten questions testing your arithmetic skills\n")#prints instructions
fName = str(input("Please Enter Your first name\n-"))# askes the user for there name
lName = str(input("Please Enter Your last name\n-"))# askes the user for there name
Class =  str(input("which class are you in?\n One, Two or Three?\n-"))#askes the user which class they are in and converts the imput into lower case
print ("Hello", fName, "you are in class", Class , "you now will be asked ten questions")


def scoresave():
    global highscore#calls the global varible
    global Class#calls the class varible
    global fName#calls the first name varible
    global lName
    global score#calls the score varible
    total = sum(highscore)#adds the high score varible
    average = (total/3)#works out the average
    highscore = str(highscore)#converts score into a str from int
    average = str(average)#converts the average into a str so it can save
    if  Class == "one":#if theyre in class one
        file = open("Scores class one.txt", "a")#opens the file scores
        file.write(fName)#writes the first name to file
        file.write(",")#writes a comma to a file
        file.write(lName)#writes the last name to the file
        file.write(",")#writes a comma to a file
        file.write(highscore)#writes the highscore to the file
        file.write(",")#writes a comma to a file
        file.write(average)#writes the average to the file
        file.write("\n")#writes the date, username and score to file for class one
        file.close()#closes the file
    elif Class == "two":#same as one
        file = open("Scores class two.txt", "a")
        file.write(fName)
        file.write(",")
        file.write(lName)
        file.write(",")
        file.write(highscore)
        file.write(",")
        file.write(average)
        file.write("\n")#writes the date, username and score to file for class one
        file.close()#closes the file
    elif  Class == "three":#same as one
        file = open("Scores class three.txt", "a")
        file.write(fName)
        file.write(",")
        file.write(lName)
        file.write(",")
        file.write(highscore)
        file.write(",")
        file.write(average)
        file.write("\n")#writes the date, username and score to file for class one
        file.close()#closes the file
    else:
        Class =  str(input("Please  enter a vaild class\n One, Two or Three?\n-"))#if the user enters the wrong class it will ask for the correct class.
        print(scoresave())

def repeate():        
    r = str(input("Would you like to take the quiz again? y/n\n-")).lower()
    if r == "y":
        print(quiz())
    elif r == "n":
        print ("\nThank you for completing this math quiz.")
        print(scoresave())
    else:
        print (repeate())

def quiz():
    global highscore
    global i
    global score
    global fName
    question = 0
    i = 10#puts the counter on ten
    score = 0
    opts = ("+", "*", "-")# for random math methods
    while i != 0:#while loop will end once run ten times for ten questons 
        i = i - 1 # takes away one from counter so it only loops ten times
        number1 = random.randint(1,10)#generates the random number for the question
        number2 = random.randint(1,10)
        sign = random.choice (opts)# generates the random math option + - *
        try: #stops error if user enters something other than a number.
            question = int(input("What is {0}{1}{2} =".format(number1,sign,number2))) #askes the user the question
        except ValueError: 
            print()
        
        if sign == "+": #tests which method was randomly generated.
            answer = (number1 + number2) # if method is plus it adds the numbers
        elif sign == "*":
            answer = (number1 * number2)
        else:
            answer = (number1 - number2)
        
        if question == answer: #checks if the user entered the correct answer.
            print ("Your answer was correct\n")
            score = score + 1 # if user gets anser correct it adds one to the score counter
        else:
            print("Your answer was Wrong the correct answer was",answer, "\n")#tells the user that they got the anser wrong and it gives them the correct answer
    highscore.append(score)
    del highscore[0]
    print (fName, "you Got",score, "out of 10")# tells the user what they got out of ten
    print("Your last three top high scores are", highscore)
    print (repeate())
print (quiz())




