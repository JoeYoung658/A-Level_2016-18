


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


Deck_One = Deck_One.returndeck()

Deck_Two = Deck_Two.returndeck()



