from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re
from datetime import date


def get_noun_list(noun_bank):
	#noun_bank = "noun_bank.txt"

	with open(noun_bank, "r") as nouns:
		noun_list = nouns.read().split("\n")[:-2:]
	#print(noun_list)
	return noun_list


def object(verb_type):
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
	decision = randint(1, 100)
	if decision % 2 == 0:
		#return noun_only(verb_type)		#noun only
		return phrase_generate(verb_type)
	else:
		#return adj_noun(verb_type)		#return adj_noun
		#print("Adj and Noun")
		return phrase_generate(verb_type, True)

def phrase_generate(verb_type, adjective=False):
	question_type = {

		"food":		"noun_food.txt", 		# eat
		"drink" :	"noun_drinks.txt", 		# drink
		"appliance":"noun_appliance.txt", 	# break / carry / hold / sit on
		"clothes":	"noun_clothing.txt"		# wear / put on / hold / wash
	}

	nouns = get_noun_list(question_type.get(verb_type, ""))
	#print(nouns)

	if not adjective:
		return f"{choice(nouns)}"
	else:
		return f"{adj_generate(verb_type)} {choice(nouns) }"

def adj_generate(verb_type):
	adjectives = {

		"food": 		["warm", "sweet", "sour", "bitter", "awful", "delicious"],
		"drink":		["sparkly", "delicious", "salty", "colorful-looking", "green"],
		"appliance":	["comfortable", "beautiful", "fun-looking",],
		"clothes":		["beautiful", "warm", "cozy", "sparkly", "lovely", "white", "blue", "red"]

	}

	#adjective = choice(adjectives.get(verb_type,""))
	#print(adjective)
	return f"{choice(adjectives.get(verb_type,''))}"













