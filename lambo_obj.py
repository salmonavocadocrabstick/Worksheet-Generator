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

def scrape_noun_list():
	noun_url = "https://stickyball.net/esl-grammar-worksheets.html?id=85"
	res = requests.get(noun_url)


	soup = BeautifulSoup(res.text, "html.parser")
			# nouns = soup.find(class_="item-page").select("p")[firstword].get_text()
	records = soup.find(class_="item-page").select("p")
	pattern = re.compile(r"^[0-9]{1,3}\.\s(\b[a-z]*\b$)")

	with open(noun_bank, "w") as noun_file:
		for word in range(2, len(records)-1):
			match = pattern.search(records[word].get_text())
			if match:
				regex_word = pattern.sub("\g<1>", records[word].get_text())
				noun_file.write(regex_word + " ")


def object():
	decision = randint(1, 5)
	if decision < 2:
		#singular
		return f"a {noun_or_adj_noun()}"
	else:
		#plural
		return f"{decision} {noun_or_adj_noun()}s"


def noun_or_adj_noun():
	decision = randint(1, 100)
	if decision % 2 == 0:
		return noun_only()		#noun only
	else:
		return adj_noun()		#return adj_noun

def noun_only():
	question_type = [

		"noun_food.txt" 		# eat
		"noun_drink.txt", 		# drink
		"noun_appliance.txt", 	# break / carry / hold / sit on
		"noun_clothing.txt"		# wear / put on / hold / wash

	]
			
	this_question = choice(question_type)

	nouns = get_noun_list(this_question)
	return f"{choice(nouns)}"

def adj_noun():
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
	nouns = get_noun_list()
	return f"{choice(adjectives)} {choice(nouns)}"













