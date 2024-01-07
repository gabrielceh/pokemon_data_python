import csv
from pokemon_data import pokemon
from graphics import bars_pokemon
import modules.info as info


if __name__ == "__main__":
	print("**** Bienvenido a Pokémon Data ***")
	pokemon_list = pokemon.get_pokemon_list()
	while True:
		opt =	info.show_menu()
		if opt == "1":
			bars_pokemon.generate_bars_types_totals(pokemon_list)
		elif opt == "2":
			bars_pokemon.generate_bars_types_totals(pokemon_list, is_secondary=True)
		elif opt == "3":
			pok = info.select_pokemon(pokemon.get_pokemon_by_name, pokemon.get_pokemon_by_pokedex_number)
			if pok:
				bars_pokemon.generate_bars_stats_pokemon(pok)
			else:
				print(f"No se encontro a este Pokémon")
		else:
			print("Opción no valida")
			continue
		
		cont = input("\nDesea continuar? S/N ")
		if cont.lower() == "n":
			print("Gracias por probar el programa")
			break
		else:
			info.clear_console()

		
