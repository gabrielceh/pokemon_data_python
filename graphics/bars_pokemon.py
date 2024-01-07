import matplotlib.pyplot as plt

_types = [
		"bug",
		"dark",
		"dragon",
		"electric",
		"fairy",
		"fighting",
		"fire",
		"flying",
		"ghost",
		"grass",
		"ground",
		"ice",
		"normal",
		"poison",
		"psychic",
		"rock",
		"steel",
		"water", 
		"none"
]
_types_colors = {
	"bug":"#A8B821",
		"dark":"#705949",
		"dragon":"#7039F8",
		"electric":"#F8D130",
		"fairy":"#EF99AC",
		"fighting":"#C13128",
		"fire":"#F18031",
		"flying":"#A990F0",
		"ghost":"#705999",
		"grass":"#78C850",
		"ground":"#E1C068",
		"ice":"#99D8D8",
		"normal":"#A9A878",
		"poison":"#A041A1",
		"psychic":"#F95889",
		"rock":"#B8A138",
		"steel":"#B9B8D1",
		"water":"#6891F0",
		"none":"#000000"
}

_types_count = {
		"bug":0,
		"dark":0,
		"dragon":0,
		"electric":0,
		"fairy":0,
		"fighting":0,
		"fire":0,
		"flying":0,
		"ghost":0,
		"grass":0,
		"ground":0,
		"ice":0,
		"normal":0,
		"poison":0,
		"psychic":0,
		"rock":0,
		"steel":0,
		"water":0,
		"none":0
	}

def _get_types_totals(list_pokemon, is_secondary = False):
	type_data = "PrimaryType" if not is_secondary else "SecondaryType"
	types = list(map(lambda x: x[type_data], list_pokemon))
	types_count = _types_count.copy()	
	for t in types:
		if t == "":
			types_count["none"] += 1
		elif t in types_count:
			types_count[t] += 1
	return types_count
	

def generate_bars_types_totals(list_pokemon, is_secondary=False):
	types_count = _get_types_totals(list_pokemon, is_secondary)
	types = list(types_count.keys())
	values = list(types_count.values())

	fig, ax = plt.subplots()
	ax.bar(types, values, color=list(_types_colors.values()))
	ax.set_ylabel("Quantity")
	ax.set_xlabel("Types")
	ax.set_title("Primary Types Quantity Pokemon")
	plt.show()

def generate_bars_stats_pokemon(pokemon_dict):
	stats = {
		"HP":int(pokemon_dict["HP"]),
		"Att":int(pokemon_dict["Att"]),
		"Def":int(pokemon_dict["Def"]),
		"S.Att":int(pokemon_dict["S.Att"]),
		"S.Def":int(pokemon_dict["S.Def"]),
		"Spd":int(pokemon_dict["Spd"])
	}
	labels = list(stats.keys())
	values = list(stats.values())
	max_stat_index = values.index(max(values))
	colors = ["#6891F0","#6891F0","#6891F0","#6891F0","#6891F0"]
	colors.insert(max_stat_index,"#C13128")

	fig, ax = plt.subplots()
	ax.bar(labels, values, color=colors)
	ax.set_title(f"{pokemon_dict['Name']} Stats")
	ax.grid(True)
	plt.show()