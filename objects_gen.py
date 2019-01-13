from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import nouns_gen as noun

def object(verb_type, decision=-99):
	'''Rolls for singular / plural nouns, and branches into generating noun+adjs. Depending on the verb type, may return a slightly different string due to uncountable nouns.'''
	if decision == -99:
		decision = randint(1, 5)

	if decision < 2:
		#singular
		if verb_type == "drink":
			return f"a bottle of {noun_or_adj_noun(verb_type)} juice"
		else:
			return f"a {noun_or_adj_noun(verb_type)}"


	else:
		#plural
		if verb_type == "drink":
			return f"{decision} cups of {noun_or_adj_noun(verb_type)} juice"
		else:
			return f"{decision} {noun_or_adj_noun(verb_type)}s"


def noun_or_adj_noun(verb_type):
	'''Rolls for adj or adj + noun. Branches into phrase_generate. 1 parameter required, but used in this function. It is passed intwo phrase_generate'''
	decision = randint(1, 100)
	if decision % 2 == 0:
		return phrase_generate(verb_type)		#No adjectives
	else:
		return phrase_generate(verb_type, True)	#Adjectives + noun



def phrase_generate(verb_type, adjective=False):
	'''Takes a key, and grabs corresponding txt file to generate a phrase of adj or adj + nouns. Note that adjectives are defaulting to False.'''
	noun_file_names = {

		"food":		"noun_food.txt", 		# eat
		"drink" :	"noun_drinks.txt", 		# drink
		"appliance":"noun_appliance.txt", 	# break / carry / hold / sit on
		"clothes":	"noun_clothing.txt"		# wear / put on / hold / wash
	}

	nouns = noun.get_noun_list(noun_file_names.get(verb_type, ""))

	if not adjective:
		return f"{choice(nouns)}"
	else:
		return f"{adj_generate(verb_type)} {choice(nouns) }"


def adj_generate(verb_type):
	'''Takes a key, and grabs random choice from the corresponding list of adjectives'''
	adjective_list = {

		"food": 		["warm", "sweet", "sour", "bitter", "awful", "delicious"],
		"drink":		["sparkly", "delicious", "salty", "colorful-looking", "green"],
		"appliance":	["comfortable", "beautiful", "fun-looking",],
		"clothes":		["beautiful", "warm", "cozy", "sparkly", "lovely", "white", "blue", "red"]

	}

	return f"{choice(adjective_list.get(verb_type,''))}"













