import platform
import os

def show_menu():
	selection =input("""Selecciona lo que quieres visualizar:
			 [1] : Mostrar la cantida de Pokémon por tipo principal
			 [2] : Mostrar la cantida de Pokémon por tipo Secundario
			 [3] : Buscar un Pokemon en especifico y mostrar sus stats
			 """)
	
	return selection


def select_pokemon(fn_name, fn_id):
	poke = input("""Ingrese el nombre o id del Pokémon: """)
	pokemon = fn_id(poke) if poke.isdigit() else fn_name(poke) 
	return pokemon


def clear_console():
	op_sys = platform.system()
	if op_sys == "Windows":
			os.system('cls')
	else:
		os.system('clear')