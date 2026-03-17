from flask import Flask, request, jsonify, render_template
from game import Game

app = Flask(__name__)

# Initialize game variable
game = None

def init_game():
    """Initialize a new game with 4 players"""
    global game
    game = Game()
    return game

@app.route('/')
def index():
    # Reset game state when page is loaded
    init_game()
    return render_template('index.html'
                           #, 
                        #  players=game.players,
                        #  green_card=game.current_green_card,
                        #  current_judge=game.current_judge
                        )

@app.route('/game_state')
def game_state():
    return jsonify(game.get_game_state())

@app.route('/play_card', methods=['POST'])
def play_card():
    print("play_card")
    data = request.json
    player_id = data['player_id']
    card_id = data['card_id']
    success = game.play_card(player_id, card_id)
    return jsonify({'success': success})

@app.route('/judge_round', methods=['POST'])
def judge_round():
    print("judge_round")
    data = request.json
    winner_id = data['winner_id']
    success = game.judge_round(winner_id)
    return jsonify({'success': success})

if __name__ == '__main__':
    init_game()  # Initialize game when server starts
    app.run(host='0.0.0.0', port=5004, debug=True) 