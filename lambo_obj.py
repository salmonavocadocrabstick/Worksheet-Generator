from random import choice, randint

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
