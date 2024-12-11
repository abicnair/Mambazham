class Player:
    def __init__(self, player_id, name):
        self.id = player_id
        self.name = name
        self.hand = []
        self.score = 0

    def to_dict(self):
        hand_dict = [card.to_dict() for card in self.hand]
        return {
            'id': self.id,
            'name': self.name,
            'hand': hand_dict,
            'score': self.score
        }

    def play_card(self, card_id):
        """Remove and return a specific card from player's hand"""
        for i, card in enumerate(self.hand):
            if card.id == card_id:
                return self.hand.pop(i)
        return None 