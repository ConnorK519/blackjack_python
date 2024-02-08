from player import Player


class Dealer(Player):
    def __init__(self, deck):
        super().__init__("Dealer")
        self.deck = deck
        self.deck.shuffle()

    def deal_card(self, hand):
        card = self.deck.draw_card()
        hand.append(card)

    def stand(self):
        self.update_score()
        return self.score >= 17
