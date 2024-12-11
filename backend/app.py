from flask import Flask, request, jsonify
from flask_cors import CORS
from game import Game

app = Flask(__name__)
CORS(app)

games = {}

@app.route('/create_game', methods=['POST'])
def create_game():
    game_id = len(games) + 1
    games[game_id] = Game()
    return jsonify({'game_id': game_id})

@app.route('/join_game', methods=['POST'])
def join_game():
    data = request.json
    game_id = data['game_id']
    player_name = data['player_name']
    
    if game_id in games:
        player_id = len(games[game_id].players) + 1
        if games[game_id].add_player(player_id, player_name):
            return jsonify({
                'player_id': player_id,
                'hand': games[game_id].players[player_id]['hand']
            })
    return jsonify({'error': 'Game full or not found'}), 400

@app.route('/start_round', methods=['POST'])
def start_round():
    data = request.json
    game_id = data['game_id']
    
    if game_id in games:
        games[game_id].start_round()
        return jsonify({
            'green_card': games[game_id].current_green_card,
            'judge': games[game_id].current_judge
        })
    return jsonify({'error': 'Game not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
