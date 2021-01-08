from flask import Flask, jsonify

app = Flask(__name__)

mock_list_db = [
    {
        "pokemon_id": "0",
        "name": "Mew",
        "level": 5,
        "description": "A special, mythical creature.",
        "in_party": True
    },
    {
        "pokemon_id": "1",
        "name": "Pikachu",
        "level": 32,
        "description": "A true rascal in nature.",
        "in_party": True
    },
    {
        "pokemon_id": "2",
        "name": "Poliwhirl",
        "level": 28,
        "description": "One of the best.",
        "in_party": False
    }
]

# http://127.0.0.1:5000/
@app.route("/")
def index():
    return "Welcome to the API!"


# http://127.0.0.1:5000/pokemon_list
@app.route("/pokemon_list", methods=['GET'])
def get_pokemon_list():
    return jsonify({"Pokemon": mock_list_db})


# http://127.0.0.1:5000/pokemon_list/0
@app.route("/pokemon_list/<int:index>", methods=['GET'])
def get_pokemon_by_index(index):
    return jsonify({"Pokemon": mock_list_db[index]})


if __name__ == "__main__":
    app.run(debug=True)