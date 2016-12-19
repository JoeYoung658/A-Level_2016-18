""" Classes. V.1 Joe Young """

RANKS = { 1  :  "Ace",
          2  :  "2",
          3  :  "3",
          4  :  "4",
          5  :  "5",
          6  :  "6",
          7  :  "7",
          8  :  "8",
          9  :  "9",
          10 :  "J",
          11 :  "Q",
          12 :  "K"}

SUITS = { 1 : "Hearts",
          2 : "Spades",
          3 : "Clubs",
          4 : "Diamonds"}          


class card():
    global RANKS
    global SUITS
    def __init__(self, rank, suit):
        rank = (RANKS[rank])
        suit = (SUITS[suit])
        self.rank = rank
        self.suit = suit

    def print_card(self):
        print("Rank:", self.rank)
        print("Suit:", self.suit)


def main():
    Deck = []
    for suit in range(1, 4):
        for rank in range(1, 13):
            Deck.append(card(rank, suit))   
    for card in Deck:
        print(card.rank, card.suit)

if __name__ == "__main__":
    main()