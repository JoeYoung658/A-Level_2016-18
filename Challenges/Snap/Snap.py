import random
import time


"""
 * Created by josep on 18/10/2017.
 """

class Card():
    _RANKS = { 1  :  "Ace",
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
    _SUITS = { 1 : "Clubs",
          2 : "Diamonds",
          3 : "Hearts",
          4 : "Spades"} 


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return(self._RANKS[self.rank] + " of " + self._SUITS[self.suit])

    def get_rank(self):
        return(self._RANKS[self.rank])

    def get_suit(self):
        return(self._SUITS[self.suit])


class Deck():
    def __init__(self):
        self.cards = []
        self._populate()
        
    def _populate(self):
        for suit in range(1, 5):
            for rank in range(1, 14):
                self.cards.append(Card(rank,suit))

    def display(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)


def main():
    my_deck = Deck()
    #my_deck.display()
    my_deck.shuffle()
    #my_deck.display()

    
    for i in range(0,len(my_deck.cards) - 1):
        current_card = my_deck.cards[i]
        next_card = my_deck.cards[i + 1]

        print("---")
        print(current_card)
        #time.sleep(0.5)
        print(next_card)
        print("---")
        
        if(current_card.get_rank() == next_card.get_rank()):
            print("Ranks Match - Snap!")
            
    
if __name__ == "__main__":
    main()
