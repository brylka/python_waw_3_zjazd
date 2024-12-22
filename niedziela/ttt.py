from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tictactoe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moves = db.Column(db.String, default="")

with app.app_context():
    db.create_all()

@app.route('/game', methods=['POST'])
def create_game():
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    return jsonify({'message': 'New game created', 'game_id': new_game.id}), 201

@app.route('/game/<int:game_id>/move', methods=['POST'])
def make_move(game_id):
    game = Game.query.get(game_id)
    if game is None:
        return jsonify({'error': 'Game not found'}), 404
    move_data = request.json
    if 'cellIndex' in move_data:
        cell_index = str(move_data['cellIndex'])

        occupied_cells = [move[0] for move in game.moves]
        if cell_index in occupied_cells:
            return jsonify({'message': 'Cell is already occupied'}), 400

        player = 'O' if game.moves.count('X') > game.moves.count('O') else 'X'
        move = f"{cell_index}{player}"
        game.moves += move
        db.session.commit()
        return jsonify({'message': 'Move made', 'game_id': game.id, 'moves': game.moves}), 200
    else:
        return jsonify({'message': 'Move data is required'}), 400


@app.route('/game/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    if game is None:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify({'game_id': game.id, 'moves': game.moves}), 200

if __name__ == '__main__':
    app.run(debug=True)