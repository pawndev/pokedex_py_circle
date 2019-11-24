class Pokedex:
    pokemons = []

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def get_by_(self, attribute: str, attribute_value):
        return next(poke for poke in self.pokemons if getattr(poke, attribute) == attribute_value)

    def get_by_id(self, id: int):
        return self.get_by_("id", id)

    def get_by_name(self, name: str):
        return self.get_by_("name", name)

    def serialize(self):
        return [p.serialize() for p in self.pokemons]
