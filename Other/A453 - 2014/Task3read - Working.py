#Joseph Young - 1413

def one():
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
        print("Class data for One was not found!\n")
        print("\n")
    return (option())

def two():
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
    return (option())


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
    return (option())


def option():
    Class = str(input("Which class would you like to see the data for? One, Two or Three.\n(Type exit to exit the program)\n-")).title()
    if Class == "One":
        print ("Here is the data for class One.\n")
        print (one())
    elif Class == "Two":
        print ("Here is the data for class Two.\n")
        print (two())
    elif Class == "Three":
        print ("Here is the data for class Three.\n")
        print (three())
    elif Class == "Exit":
        print ("You have Exited the program")
    else:
        print ("Please enter a vaild class name")
        return (option())
print (option())
