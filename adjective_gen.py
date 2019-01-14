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
		"clothes":		["golden", "dark", "maroon", "beige", "navy", "mint", "brown"]

	}

	return f"{choice(color_adjective_list.get(item_type,''))}"



def quantity_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	quantity_adjective_list = {

		"food": 		["a", "two", "three"],
		"drink":		["four", "a", "two", "three"],
		"appliance":	["a single", "five", "two", "many"],
		"clothes":		["a lot of", "many", "ten"]

	}

	return f"{choice(quantity_adjective_list.get(item_type,''))}"

def quality_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	quality_adjective_list = {

		"food": 		["delicious", "tasty", "disgusting", "sour"],	#NOTE: need to come back and fix this silliness
		"drink":		["sweet", "salty", "gross", "yummy"],
		"appliance":	["new", "used", "old", "broken"],
		"clothes":		["new", "used", "old", "patchy"]

	}

	return f"{choice(quality_adjective_list.get(item_type,''))}"

def size_adj_generator(item_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	quantity_adjective_list = {

		"food": 		["large", "small", "huge", "tiny"],	#NOTE: need to come back and fix this silliness
		"drink":		["large", "small", "huge", "tiny"],
		"appliance":	["large", "small", "huge", "tiny"],
		"clothes":		["large", "small", "huge", "tiny"]

	}

	return f"{choice(quantity_adjective_list.get(item_type,''))}"

def purpose_adj_generator(item_type):
	quantity_adjective_list = {

		"food": 		["large", "small", "huge", "tiny"],	#NOTE: need to come back and fix this silliness
		"drink":		["large", "small", "huge", "tiny"],
		"appliance":	["large", "small", "huge", "tiny"],
		"clothes":		["large", "small", "huge", "tiny"]

	}
	return f"{choice(quantity_adjective_list.get(item_type,''))}"





