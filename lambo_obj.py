from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re
from datetime import date


def get_noun_list(noun_bank):
	#noun_bank = "noun_bank.txt"

	with open(noun_bank, "r") as nouns:
		noun_list = nouns.read().split("\n")[:-2:]
	return noun_list


def object(verb_type):
	decision = randint(1, 5)
	if decision < 2:
		#singular
		return f"a {noun_or_adj_noun(verb_type)}"
	else:
		#plural
		return f"{decision} {noun_or_adj_noun(verb_type)}s"


def noun_or_adj_noun(verb_type):
	decision = randint(1, 100)
	if decision % 2 == 0:
		return noun_only(verb_type)		#noun only
	else:
		return adj_noun(verb_type)		#return adj_noun

def noun_only(verb_type):
	question_type = {

		"food":		"noun_food.txt", 		# eat
		"drink" :	"noun_drinks.txt", 		# drink
		"appliance":"noun_appliance.txt", 	# break / carry / hold / sit on
		"clothes":	"noun_clothing.txt"		# wear / put on / hold / wash

	}

	nouns = get_noun_list(question_type.get(verb_type, ""))
	return f"{choice(nouns)}"

def adj_noun(verb_type):
	adjectives = [
				"warm",
				"cozy",
				"comfortable",
				"lovely",
				"beautiful",
				"sparkly",
				"fun-looking",
				"white",
				"blue",
				"red"
			]

	question_type = {  

		"food":		"noun_food.txt", 		# eat
		"drink" :	"noun_drinks.txt", 		# drink
		"appliance":"noun_appliance.txt", 	# break / carry / hold / sit on
		"clothes":	"noun_clothing.txt"		# wear / put on / hold / wash

	}
	#this_question = choice(question_type)
	nouns = get_noun_list(question_type.get(verb_type, ""))
	return f"{choice(adjectives)} {choice(nouns)}"













