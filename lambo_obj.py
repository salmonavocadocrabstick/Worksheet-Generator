from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re
from datetime import date

nouns = 	[
				"jacket",
				"jumper",
				"sneaker",
				"sunglasses",
				"skirt",
				"bracelet",
				"ring",
				"egg",
				"juice"
			]


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

pract_str=""

def object():
	decision = randint(1, 5)
	if decision < 2:
		return f"a {noun_or_adj_noun()}"
	else:
		return f"{decision} {noun_or_adj_noun()}s"


def noun_or_adj_noun():
	decision = randint(1, 100)
	if decision % 2 == 0:
		return noun_only()		#noun only
	else:
		return adj_noun()		#return adj_noun

def noun_only():
	return f"{choice(nouns)}"

def adj_noun():
	return f"{choice(adjectives)} {choice(nouns)}"


timestamp = "time_record.txt"
noun_bank = "noun_bank.txt"

today = date.today()
need_to_scrape = False

try:
	with open(timestamp, "r+") as time_file:
		last_time = time_file.read()
		last_time = last_time.split("-")
		#print(last_time)
		if date(today.year, today.month, 28) > date(int(last_time[0]), int(last_time[1]), 28):
			time_file.seek(0)
			time_file.write(str(today))
			need_to_scrape = True

except FileNotFoundError:
	pass


noun_url = "https://stickyball.net/esl-grammar-worksheets.html?id=85"
res = requests.get(noun_url)


soup = BeautifulSoup(res.text, "html.parser")
		# nouns = soup.find(class_="item-page").select("p")[firstword].get_text()
records = soup.find(class_="item-page").select("p")
text_only = []
pattern = re.compile(r"^[0-9]{1,3}\.\s(\b[a-z]*\b$)")

with open(noun_bank, "w") as noun_file:
	for word in range(2, len(records)-1):
		match = pattern.search(records[word].get_text())
		if match:
			regex_word = pattern.sub("\g<1>", records[word].get_text())
			#text_only.append(regex_word)
			noun_file.write(regex_word)






#print(text_only)





