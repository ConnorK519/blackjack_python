

class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.hand = []
        self.score = 0

    def is_player_bust(self):
        return self.score > 21

    def check_for_ace(self):
        for card in self.hand:
            if card["card_value"] == 11:
                card["card_value"] = 1
                self.score -= 10
                break

    def update_score(self):
        self.score = sum(obj["card_value"] for obj in self.hand)
        if self.score > 21:
            self.check_for_ace()


