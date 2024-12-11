import random
from cards import Deck
from cards import GreenDeck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.green_deck = GreenDeck()
        # self.scores = {1: 0, 2: 0, 3: 0, 4: 0}
        self.current_judge = 1
        self.played_cards = {}
        self.round_winner = None
        
        # Initialize all 4 players
        self.players = {
            1: Player(1, "Player 1"),
            2: Player(2, "Player 2"),
            3: Player(3, "Player 3"),
            4: Player(4, "Player 4")
        }
        
        self.current_green_card = self.green_deck.draw()
        self.deal_cards()

    def judge_round(self, winning_player_id):
        print("judge_round", winning_player_id)
        if winning_player_id in self.players:
            winner = self.players[winning_player_id]
            winner.score += 1  # Update score in Player object
            self.round_winner = winning_player_id

            # Deal new cards to all players who played
            for player_id in self.played_cards.keys():
                self.players[player_id].hand.append(self.deck.draw())
            # Rotate judge
            self.current_judge = (self.current_judge % 4) + 1
            self.played_cards = {}
            # Deal new cards
            self.deal_cards()
            # Draw new green card
            self.current_green_card = self.green_deck.draw()

            return True
        return False

    def get_game_state(self):
        this_game_state = {
            'green_card': self.current_green_card.to_dict(),
            'current_judge': self.current_judge,
            'played_cards': {pid: card.to_dict() for pid, card in self.played_cards.items()},
            'round_winner': self.round_winner,  # Include round winner in game state
            'players': {pid: player.to_dict() for pid, player in self.players.items()}
        }
        print("this_game_state", this_game_state)
        return this_game_state
    
    # def deal_cards(self, count):
    #     return random.sample(self.cards.red_cards, count)
    

    def deal_cards(self):
        self.round_winner = None  # Reset round winner when dealing new cards
        for player in self.players.values():
            while len(player.hand) < 7:
                player.hand.append(self.deck.draw())

    def play_card(self, player_id, card_id):
        print("play_card", player_id, card_id)
        if player_id != self.current_judge and player_id not in self.played_cards:
            player = self.players[player_id]
            played_card = player.play_card(card_id)
            
            if played_card:
                self.played_cards[player_id] = played_card
                return True
        return False