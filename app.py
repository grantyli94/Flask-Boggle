from flask import Flask, request, render_template, jsonify, session
from uuid import uuid4


from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.route("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.route("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    
    # creates entry in games dictionary with game object (line 10)
    games[game_id] = game 

    return jsonify({"gameId": game_id, "board": game.board})

@app.route("/api/score-word", methods=["POST"])
def score_word():
    """ Checks if word from POST request is a valid word and on the board"""

    id = request.json["gameId"]
    word = request.json["word"]
    is_on_word_list = games[id].is_word_in_word_list(word)
    is_on_board = games[id].check_word_on_board(word)

    if is_on_word_list and is_on_board:
        return jsonify({"result": "ok"})
    elif not is_on_board:
        return jsonify({"result": "not-on-board"})
    else:
        return jsonify({"result": "not-word"})