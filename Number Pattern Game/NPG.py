# 09/09/2016
# Joe Young
import random
import time


count = 0
alist = []
randomc = 0



while randomc != 4:
    ran = random.randint(1, 100)
    alist.append(ran)
    randomc = randomc + 1
alist.sort()


def question():
    global alist
    global count
    number = 0
    clist = len(alist) - 1
    print(alist)
    try:
        number = int(input("Input a number which fits the sequence \n -"))
    except ValueError:
        print("Please input a whole number!\n")
        print(question())

    if number > alist[clist]:
        if count == 4:
            exit = str(input("Would you like to exit? (Yes/No)")).lower()
            if exit == "yes":
                print("You have exited the program!")
                time.sleep(5)
            elif exit == "no":
                print("You have chosen not to exit the program!")
                time.sleep(3)
                count = 0
                return question()
            else:
                print("Please enter a valid option!")
        else:
            count = count + 1
            print("Yes,", number, " does fit the sequence \n")
            return question()
    else:
        print("No,", number, " does not fit the sequence \n")
        return question()


question()
