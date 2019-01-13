# Generate nouns
#
# Stephanie Leung (2019)
from random import choice

def get_noun_list(noun_bank):
	'''Returns a designated (pre-scraped) noun list as a long list'''
	with open(noun_bank, "r") as nouns:
		noun_list = nouns.read().split("\n")[:-2:]
	return noun_list


def noun_generate(item_type):
	'''Takes a key, and grabs corresponding txt file to generate a phrase of adj or adj + nouns. Note that adjectives are defaulting to False.'''
	noun_file_names = {

		"food":		"noun_food.txt", 		# eat
		"drink" :	"noun_drinks.txt", 		# drink
		"appliance":"noun_appliance.txt", 	# break / carry / hold / sit on
		"clothes":	"noun_clothing.txt"		# wear / put on / hold / wash
	}

	nouns = get_noun_list(noun_file_names.get(item_type, ""))

	return f"{choice(nouns)}"