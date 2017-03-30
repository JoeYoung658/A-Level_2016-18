""" Classes. V.2 Joe Young """

N_SUITS = 4
N_RANKS = 13
RANKS = { 1  :  "Ace",
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
SUITS = { 1 : "Clubs",
          2 : "Diamonds",
          3 : "Hearts",
          4 : "Spades"}          

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def print_card(self):
        print(RANKS[self.rank] + " of " + SUITS[self.suit])

class Deck():
    def __init__(self):
        self.card_list = [Card(rank,suit) for rank in range(1, N_RANKS + 1) for suit in range(1, N_SUITS + 1)]

       
deck = Deck()
for card in deck.card_list:
    card.print_card()
