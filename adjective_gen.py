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
		"drink":		["sparkly", "delicious", "salty", "colorful-looking", "green"],
		"appliance":	["comfortable", "beautiful", "fun-looking",],
		"clothes":		["golden", "dark", "maroon", "lovely", "navy", "mint", "brown"]

	}

	return f"{choice(color_adjective_list.get(item_type,''))}"

def quantity_adj_generator(item_type):
	pass

def size_adj_generator(item_type):
	pass

def purpose_adj_generator(item_type):
	pass





