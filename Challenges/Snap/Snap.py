import random
import time


"""
 * Created by josep on 21/01/2017.
 """

class Card():
    def __init__(self, rank, suit):
        self.rank
        self.suit


class Deck():
    def __init__(self):
        self.RANKS = { 1  :  "Ace",
          2  :  "Two",
          3  :  "Three",
          4  :  "Four",
          5  :  "Five",
          6  :  "Six",
          7  :  "Seven",
          8  :  "Eight",
          9  :  "Nine",
          10 :  "Ten",
          11 :  "Jack",
          12 :  "Queen",
          13 :  "King"}
        self.SUITS = { 1 : "Clubs",
          2 : "Diamonds",
          3 : "Hearts",
          4 : "Spades"} 
        self.cards = []
        self._populate()

    def _populate(self):
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.cards.append((self.SUITS[suit],self.RANKS[rank]))

    def display(self):
        print(self.cards)

    def returndeck(self):
        return self.cards

def intro():
    """Prints the instructions"""
    print("----------------------------")
    print("Press enter when you see a matching card")
    print("Press enter when ready!")
    print("----------------------------")
    #input("")




def main():
    Deck_One = Deck().returndeck()
    Deck_Two = Deck().returndeck()
    
    
    game_not_over = True
    
    
    while game_not_over:
        random_1 = random.randrange(0,len(Deck_One))
        random_2 = random.randrange(0,len(Deck_Two))
        
        if (Deck_One[random_1][1] == Deck_Two[random_2][1]):
            print("Snap!")
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()