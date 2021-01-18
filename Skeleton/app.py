from flask import Flask, jsonify, request

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
    }
]

# http://127.0.0.1:5000/
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        json_received = request.get_json()
        return jsonify({"JSON Sent": json_received}), 201
    else:
        return "Welcome to the API!", 200


# http://127.0.0.1:5000/multiply/5
@app.route("/multiply/<int:value>", methods=['GET'])
def multiply_10(value):
    return jsonify({"Result": value*10}), 200


# http://127.0.0.1:5000/pokemon_list
@app.route("/pokemon_list", methods=['GET'])
def get_pokemon_list():
    return jsonify({"Pokemon": mock_list_db}), 200


# http://127.0.0.1:5000/pokemon_list/0
@app.route("/pokemon_list/<int:index>", methods=['GET'])
def get_pokemon_by_index(index):
    return jsonify({"Pokemon": mock_list_db[index]}), 200


# http://127.0.0.1:5000/author?name=Ian
@app.route("/author")
def get_author():
    name = request.args.get("name")
    return jsonify({"data": name}), 200


if __name__ == "__main__":
    app.run(debug=True)
