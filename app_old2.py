from flask import Flask, session, request, jsonify, redirect, url_for, render_template
import secrets
import json
from cards import Cards
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
logging.basicConfig(level=logging.DEBUG)

# Add CORS support if needed
from flask_cors import CORS
CORS(app)

class GameSession:
    def __init__(self, session_id):
        self.session_id = session_id
        self.players = {}  # {player_id: {"name": name, "hand": [], "score": 0}}
        self.current_judge = None
        self.green_card = None
        self.played_cards = {}
        self.max_players = 4
        self.game_started = False
        self.cards = Cards()

    def to_json(self):
        return {
            'session_id': self.session_id,
            'players': self.players,
            'current_judge': self.current_judge,
            'green_card': self.green_card,
            'played_cards': self.played_cards,
            'game_started': self.game_started
        }

# Store active game sessions
game_sessions = {}  # {session_id: GameSession}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_game', methods=['POST'])
def create_game():
    session_id = secrets.token_urlsafe(6)  # Create unique game code
    game_sessions[session_id] = GameSession(session_id)
    return jsonify({
        'session_id': session_id,
        'message': 'Game created successfully'
    })

@app.route('/join_game', methods=['POST'])
def join_game():
    logging.debug("Join game endpoint called")  # Debug log
    data = request.get_json()
    logging.debug(f"Received data: {data}")  # Debug log
    
    session_id = data.get('session_id')
    player_name = data.get('player_name')
    
    if session_id not in game_sessions:
        logging.error(f"Session {session_id} not found")  # Debug log
        return jsonify({'error': 'Game session not found'}), 404
    
    game = game_sessions[session_id]
    
    if len(game.players) >= game.max_players:
        return jsonify({'error': 'Game is full'}), 400
    
    player_id = len(game.players) + 1
    game.players[player_id] = {
        "name": player_name,
        "hand": [],
        "score": 0
    }
    
    session['player_id'] = player_id
    session['session_id'] = session_id
    
    return jsonify({
        'player_id': player_id,
        'message': f'Successfully joined game as {player_name}'
    })

@app.route('/game_state')
def game_state():
    session_id = session.get('session_id')
    player_id = session.get('player_id')
    
    if not session_id or session_id not in game_sessions:
        return jsonify({'error': 'No active game session'}), 404
    
    game = game_sessions[session_id]
    
    # Hide other players' cards
    sanitized_players = {}
    for pid, player in game.players.items():
        sanitized_players[pid] = {
            "name": player["name"],
            "score": player["score"],
            "hand_size": len(player["hand"]),
            "hand": player["hand"] if pid == player_id else []
        }
    
    data = {
        'players': sanitized_players,
        'current_judge': game.current_judge,
        'green_card': game.green_card,
        'played_cards': game.played_cards if game.current_judge == player_id else len(game.played_cards),
        'game_started': game.game_started
    }
    print(data)
    return jsonify(data)

@app.route('/start_game', methods=['POST'])
def start_game():
    session_id = session.get('session_id')
    player_id = session.get('player_id')
    
    logging.debug(f"Start game request - Session ID: {session_id}, Player ID: {player_id}")
    
    if not session_id or session_id not in game_sessions:
        logging.error(f"No active game session found for {session_id}")
        return jsonify({'error': 'No active game session'}), 404
    
    game = game_sessions[session_id]
    
    logging.debug(f"Current players: {len(game.players)}")
    if len(game.players) < 2:
        logging.error("Not enough players to start game")
        return jsonify({'error': 'Need at least 2 players to start'}), 400
    
    game.game_started = True
    game.current_judge = 1
    
    # Deal initial hands
    try:
        for player in game.players.values():
            player['hand'] = [game.cards.draw_red_card() for _ in range(7)]
        
        # Draw first green card
        game.green_card = game.cards.draw_green_card()
        
        logging.debug("Game started successfully")
        return jsonify({'message': 'Game started successfully'})
    except Exception as e:
        logging.error(f"Error starting game: {str(e)}")
        return jsonify({'error': f'Failed to start game: {str(e)}'}), 500

@app.route('/play_card', methods=['POST'])
def play_card():
    data = request.get_json()
    card_id = data.get('card_id')
    session_id = session.get('session_id')
    player_id = session.get('player_id')
    
    if not session_id or session_id not in game_sessions:
        return jsonify({'error': 'No active game session'}), 404
        
    game = game_sessions[session_id]
    
    if player_id == game.current_judge:
        return jsonify({'error': 'Judge cannot play a card'}), 400
        
    if player_id in game.played_cards:
        return jsonify({'error': 'You already played a card this round'}), 400
    
    player = game.players[player_id]
    card = None
    for c in player['hand']:
        if c['id'] == card_id:
            card = c
            player['hand'].remove(c)
            break
    
    if not card:
        return jsonify({'error': 'Card not found in hand'}), 400
        
    game.played_cards[player_id] = card
    
    return jsonify({
        'message': 'Card played successfully',
        'played_cards_count': len(game.played_cards)
    })

@app.route('/judge_round', methods=['POST'])
def judge_round():
    data = request.get_json()
    winning_player_id = data.get('winning_player_id')
    session_id = session.get('session_id')
    player_id = session.get('player_id')
    
    if not session_id or session_id not in game_sessions:
        return jsonify({'error': 'No active game session'}), 404
        
    game = game_sessions[session_id]
    
    if player_id != game.current_judge:
        return jsonify({'error': 'Only the judge can select a winner'}), 403
        
    expected_players = len(game.players) - 1
    if len(game.played_cards) < expected_players:
        return jsonify({'error': 'Not all players have played yet'}), 400
        
    if winning_player_id in game.players:
        game.players[winning_player_id]['score'] += 1
        
    # Deal new cards
    for pid, player in game.players.items():
        if pid in game.played_cards:
            new_card = game.cards.draw_red_card()
            if new_card:
                player['hand'].append(new_card)
    
    game.played_cards = {}
    game.current_judge = (game.current_judge % len(game.players)) + 1
    game.green_card = game.cards.draw_green_card()
    
    return jsonify({
        'message': 'Round completed successfully',
        'new_judge': game.current_judge,
        'winner': winning_player_id
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) 