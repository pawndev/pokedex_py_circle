from models.pokemon import Pokemon


def test_instantiate_pokemon():
    pokemon = Pokemon(1, "ivysaur", 10, 130, 1)
    assert pokemon.id == 1
    assert pokemon.name == "ivysaur"