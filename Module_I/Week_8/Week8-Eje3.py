import json

def leer_pokemon():
    with open("pokemon.json", "r") as archivo:
        return json.load(archivo)


def agregar_pokemon():
    pokemones = leer_pokemon()

    nuevo_pokemon = {}
    nuevo_pokemon["name"] = {"english": input("Nombre del Pokémon: ")}
    nuevo_pokemon["type"] = [input("Tipo del Pokémon: ")]
    nuevo_pokemon["base"] = {
        "HP": int(input("HP del Pokémon: ")),
        "Attack": int(input("Ataque del Pokémon: ")),
        "Defense": int(input("Defensa del Pokémon: ")),
        "Sp. Attack": int(input("Ataque especial del Pokémon: ")),
        "Sp. Defense": int(input("Defensa especial del Pokémon: ")),
        "Speed": int(input("Velocidad del Pokémon: "))
    }

    pokemones.append(nuevo_pokemon)

    guardar_pokemon(pokemones)


def guardar_pokemon(pokemones):
    with open("pokemon.json", "w") as archivo:
        json.dump(pokemones, archivo, indent=2)
        
agregar_pokemon()