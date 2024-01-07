import csv
import os


_PATH_DATA = os.path.join(os.getcwd() + "\data\pokemon_v2.csv")

def get_pokemon_list():
	'''
	Devuelve el listado de todos los pokemon.
	'''
	pokemon_list = []
	with open(_PATH_DATA, "r") as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		headers = next(reader)
		for pokemon in reader:
			iterable = zip(headers, pokemon)
			pokemon_dict = {key: value for key, value in iterable}
			pokemon_list.append(pokemon_dict)

	return pokemon_list

def get_pokemon_by_name(pokemon_name:str):
	pokemon_list = get_pokemon_list()
	pokemon = list(filter(lambda x: x["Name"].lower() == pokemon_name.lower(), pokemon_list))
	return pokemon[0] if len(pokemon) > 0 else None

def get_pokemon_by_pokedex_number(pokedex_number:int):
	try:
		if not type(pokedex_number) == "<class 'int'>":
			raise ValueError("El número de Pokedex debe ser un entero.")
		
		pokemon_list = get_pokemon_list()
		pokemon = list(filter(lambda x: int(x["No."]) == pokedex_number, pokemon_list))
		return pokemon[0] if len(pokemon) > 0 else None
	except ValueError as err:
		return None