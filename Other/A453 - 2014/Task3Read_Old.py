#Joseph Young - 1413

def one(): # makes a sub program
    try:
        file = open("Scores class one.txt", "r")#opens the class one file
        lines = file.readlines()#reads the lines in the file
        li = int(input("How many lines are in the file that you are requesting to see?"))
        file.close()#closes the file
        file = open("Scores class one.txt", "r")#reopens the class one file
        naMe2 = [["Blank"]*li,["Blank"]*li] #tests if the file is text field is blank
        for i in range (li):#for loop
            line = file.readline()#reads the lines the the file
            data = line.split(",")# splits the data
            name = (data[1], data[0])# picks out the first and last name from the file
            score = (data[4], data[3], data[2])#gets the last three score from the file
            naMe2[0] [i] = name  #  
            naMe2[1] [i] = score #
        file.close()
        naMe2 = sorted(zip(*naMe2), key = lambda naMe2:naMe2[0], reverse=False)#sorts the name info alphanetical order
        for loop in range(li):#for loop
           print (naMe2[loop] [0], "|", naMe2 [loop] [1])#prints the data onto the shell
        return (option())#prints the option sub program
    except:
        print("\n")
        print("Class data for One was not found!\n")
        print("\n")

def two(): #same as one but for class two data
    try:
        file = open("Scores class two.txt", "r")
        lines = file.readlines()
        li = len(lines)
        file.close()
        file = open("Scores class three.txt", "r")
        naMe2 = [["Blank"]*li,["Blank"]*li]
        for i in range (li):
            line = file.readline()
            data = line.split(",")
            name = (data[1], data[0])
            score = (data[4], data[3], data[2])
            naMe2[0] [i] = name
            naMe2[1] [i] = score
        file.close()
        naMe2 = sorted(zip(*naMe2), key = lambda naMe2:naMe2[0], reverse=False)
        for loop in range(li):
            print (naMe2[loop] [0], "|", naMe2 [loop] [1])
        return (option())
    except:
        print("\n")
        print("Class data for Two was not found!\n")
        print("\n")

def three():
    try:
        file = open("Scores class one.txt", "r")
        lines = file.readlines()
        li = len(lines)
        file.close()
        file = open("Scores class one.txt", "r")
        naMe2 = [["Blank"]*li,["Blank"]*li]
        for i in range (li):
            line = file.readline()
            data = line.split(",")
            name = (data[1], data[0])
            score = (data[4], data[3], data[2])
            naMe2[0] [i] = name
            naMe2[1] [i] = score
        file.close()
        naMe2 = sorted(zip(*naMe2), key = lambda naMe2:naMe2[0], reverse=False)
        for loop in range(li):
            print (naMe2[loop] [0], "|", naMe2 [loop] [1])
        return (option())
    except:
        print("\n")
        print("Class data for Two was not found!\n")
        print("\n")
def option(): # creates a sub program
    Class = str(input("Which class would you like to see the data for? One, Two or Three.\n(Type exit to exit the program)\n-")).title()# asks the user which class data they would like to see
    if Class == "One":# if use inputs one
        print ("Here is the data for class One.\n") # prints this into shell
        print (one())#runs the one sub program to print the data
    elif Class == "Two":# if user inputs two
        print ("Here is the data for class Two.\n")
        print (two())
    elif Class == "Three":# if user inputs three
        print ("Here is the data for class Three.\n")
        print (three())
    elif Class == "Exit": # if user inputs exit
        print ("You have Exited the program")
    else:
        print ("Please enter a vaild class name")
        return (option())
print (option())
