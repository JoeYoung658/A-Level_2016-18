import random



symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]   
player_credit = 100
cost_of_turn = 20


def random_symbols(symbols):
        """
        Generates a random symbol from a given list
       """
        return symbols[random.randint(0,len(symbols)-1)]


while player_credit > 0:

        #Checks if the player wants to play again or cash out
        print("Current Winngs =", player_credit)
        player_option = input("(C)ash out or anykey to continue")
        if (player_option == "C"):
                player_credit = 0




        #Charges the player for the turn
        player_credit -= cost_of_turn
        print("Charge of go 20p. New credit =", player_credit)

        

        #gen_symbols = [random_symbols(symbols),random_symbols(symbols),random_symbols(symbols)]
        gen_symbols = ["Skull","Lemon","Skull"]
        print(gen_symbols)
        
        
        #Checks if three of the symbols match
        if (gen_symbols[0] == gen_symbols[1] == gen_symbols[2]):
                if (gen_symbols[0] == symbols[1]):
                        player_credit += 500
                        print("Three Bells - Winnings of £5")

                elif (gen_symbols[0] == symbols[5]):
                        player_credit = 0
                        print("Three Skulls - Lost all credit")
                else:
                        
                        player_credit += 100
                        print("Three of the same symbols - Won £1")



        #Checks if two symbols match
        elif (gen_symbols[0] == gen_symbols[1] or gen_symbols[0] == gen_symbols[2] or gen_symbols[1] == gen_symbols[2]):

##                for i in range(0,2):
##                        if gen_symbols[i] == symbols[5] and gen_symbols[i+1] == symbols[5]:
##                                player_credit -= 100
##                                print("Two Skulls - Lost £1")
##                                break
##
##                        else:
##                                print("Won 50p")
                
                if (gen_symbols[0] == symbols[5] and gen_symbols[1] == symbols[5]):
                        player_credit -= 100
                        print("Two Skulls - Lost £1")
                elif (gen_symbols[0] == symbols[5] and gen_symbols[2] == symbols[5]):
                        player_credit -= 100
                        print("Two Skulls - Lost £1")
                elif (gen_symbols[1] == symbols[5] and gen_symbols[2] == symbols[5]):
                        player_credit -= 100
                        print("Two Skulls - Lost £1")
                else:
                        player_credit += 50
                        print("Two of the same symbols - Won 50p")
                
        
        else:
                print("No Winnings")


        if (player_credit < 0):
                print("You've run out of credit")
                break
        
        




