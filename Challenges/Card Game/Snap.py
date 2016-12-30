""" Classes. V.1 Joe Young """
import random
import time

RANKS = { 1  :  "Ace",
          2  :  "2",
          3  :  "3",
          4  :  "4",
          5  :  "5",
          6  :  "6",
          7  :  "7",
          8  :  "8",
          9  :  "9",
          10 :  "10",
          11 :  "J",
          12 :  "Q",
          13 :  "K"}

SUITS = { 1 : "Hearts",
          2 : "Spades",
          3 : "Clubs",
          4 : "Diamonds"}          


class card():
    global RANKS
    global SUITS
    
    tdeck = []

    def __init__(self, rank, suit):
        # rank = (RANKS[rank])
        # suit = (SUITS[suit])
        self.rank = rank
        self.suit = suit
        
    def number_to_word(self):
        return (self.rank + self.suit)

    def print_card(self):
        print("Rank:", self.rank)
        print("Suit:", self.suit)


def main():
    global card
    Deck = []
    tDeck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            Deck.append(card(rank, suit))

    for card in Deck:
        tDeck.append((card.rank, card.suit))

    print(tDeck)
    print(len(Deck))
    random.shuffle(tDeck)
    print(tDeck)


if __name__ == "__main__":
    main()