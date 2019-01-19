from random import choice, randint


def verb():
	'''Generates a random verb. Returns both key and value for the adjectives and nouns to adhere too. This one doesn't use and file ios as the list is still short.'''

	verbs = {
	
	"food":				["have", "eat", "enjoy", "chew", "munch", "cut", "cook", "stir"],
	"drink":			["have", "sip", "drink", "slurp", "make"],
	"appliance":		["have", "sit on", "carry" , "break", "fix", "repair", "use", "touch" , "buy"],
	"clothes" : 		["have", "wear", "carry", "make", "hold", "put on", "sew", "knit", "fold"],
	"activities":		["go to", "have"],
	"raw_mats":			["have", "dig", "harvest", "buy", "scoop", "mix"]
	
	}

	key = choice(list(verbs))
	return [str(key), choice(verbs.get(key, ""))]


