# Generate adjectives
#
# Stephanie Leung (2019)
from random import choice

def get_adjective_list(adj_bank):
	pass
	#will implement later.


def color_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	color_adjective_list = {

		"food": 		["red", "orange", "yellow", "pink"],
		"drink":		["red", "orange", "yellow", "pink", "green", "blue", "white"],
		"appliance":	["grey", "black", "white", "silver"],
		"clothes":		["golden", "dark", "maroon", "beige", "navy", "mint", "brown"],
		"raw_mats":		["brown", "white", "light-colored", "dark-colored"]
	
	}

	return f"{choice(color_adjective_list.get(item_type,''))}"


def quality_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	quality_adjective_list = {

		"food": 		["delicious", "tasty", "disgusting", "sour"],	#NOTE: need to come back and fix this silliness
		"drink":		["sweet", "salty", "sour", "yummy"],
		"appliance":	["energy-saving", "sparkly", "efficient"],
		"clothes":		["new", "used", "old", "patchy"],
		"activities":	["fun", "interesting", "boring", "tough", "easy", "difficult"]
		

	}

	return f"{choice(quality_adjective_list.get(item_type,''))}"

def size_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	quantity_adjective_list = {

		"food": 		["large", "bite-sized", "small", "huge", "tiny"],	#NOTE: need to come back and fix this silliness
		"drink":		["large", "big", "small", "huge", "tiny"],
		"appliance":	["palm-sized", "enormous", "tiny"],
		"clothes":		["large", "small", "huge", "tiny"],
		"activities":	["one hour long", "half an hour long"],
		"raw_mats":		["heavy", "half"]

	}

	return f"{choice(quantity_adjective_list.get(item_type,''))}"

def state_adj_generator(item_type):
	quantity_adjective_list = {

		"food": 		["hearty", "filling", "buttery", "creamy"],	#NOTE: need to come back and fix this silliness
		"drink":		["fresh", "store-bought"],
		"clothes":		["warm", "cozy", "comfortable", "fitting", "elegant", "beautiful"],
		"appliance":	["new", "used", "old", "broken", "useful"]

	}
	return f"{choice(quantity_adjective_list.get(item_type,''))}"





