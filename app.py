import json
from flask import Flask, abort
from models.pokemon import Pokemon
from models.pokedex import Pokedex

app: Flask = Flask(__name__)
pokedex = Pokedex()


def generate_pokedex(file_name: str):
    """
    Load json and generate all class.

    :type file_name: pokedex json filepath
    """
    with open(file_name) as json_file:
        datas = json.load(json_file)
        print(datas)
        for pokemon_obj in datas:
            pokedex.add_pokemon(Pokemon(pokemon_obj['id'], pokemon_obj['identifier'], pokemon_obj['height'], pokemon_obj['weight'], pokemon_obj['order']))
    print("Pokedex loaded successfully !")


@app.route('/')
def home():
    return "Boulou"


@app.route('/pokemon', strict_slashes=False)
def list_all():
    return {
        'items': pokedex.serialize()
    }


@app.route('/pokemon/<int:pokemon_id>')
def get_by_id(pokemon_id: int):
    try:
        pokemon = pokedex.get_by_id(pokemon_id)
        return pokemon.serialize()
    except:
        return abort(404)


@app.route('/pokemon/name/<string:pokemon_name>')
def get_by_name(pokemon_name: str):
    try:
        pokemon = pokedex.get_by_name(pokemon_name.lower())
        return pokemon.serialize()
    except:
        return abort(404)


@app.before_first_request
def init_server():
    generate_pokedex("resources/pokedex.json")


if __name__ == '__main__':
    app.run()
