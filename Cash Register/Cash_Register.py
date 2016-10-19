"""
Joe Young
Cash Register V.1
"""

dict_register = {  "£50" : 3,
              "£20" : 5,
              "£10" : 12,
               "£5" : 10,
               "£2" : 15,
               "£1" : 20,
             "£0.50" : 5,
             "£0.20" : 20,
             "£0.10" : 30,
            "£0.05" : 10,
            "£0.02" : 15,
            "£0.01" : 10
           }

register = [ [50, 3], 
             [20, 5],
             [10, 12],
             [5, 10],
             [2, 15],
             [1, 20],
             [0.50, 5],
             [0.2, 20],
             [0.1, 30],
             [0.05, 10],
             [0.02, 15],
             [0.01, 10]
           ] 
change_due = 105.69 #This is the value that needs to be accumulated from coins and notes.

def calc_change(change_due, register):
    """ Function to figure out the amount of coins. 
    """ 
    for cash in range(len(register)): #A for loop to run the while loop for every coin/note in the register.
        count=0
        #Figures out how many of each coin/note needs to be given in order to achieve the change due.
        while change_due > register[cash][0] and register[cash][1] > 0:
            change_due -= register[cash][0]
            register[cash][1] -= 1
            count+=1
        if not(count == 0):
            print ("You need to give",count, "£"+ str(register[cash][0]))

print(change_due, "In total due.")
calc_change(change_due, register)
