import random


class Deck:
    def __init__(self, num_of_decks=1):
        self.card_prefixes = ["Ace of", "Two of", "Three of", "Four of", "Five of", "Six of", "Seven of",
                              "Eight of", "Nine of", "Ten of", "Jack of", "Queen of", "King of"]
        self.card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self.deck = []
        self.build_deck(num_of_decks)

    def build_deck(self, num_of_decks):
        for _ in range(num_of_decks):
            for suit in self.suits:
                for i in range(len(self.card_prefixes)):
                    self.deck.append(
                        {"card_name": f"{self.card_prefixes[i]} {suit}", "card_value": self.card_values[i]})

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()
