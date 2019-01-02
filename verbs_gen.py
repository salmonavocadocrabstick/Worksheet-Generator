from random import choice, randint


def verb():
	'''Generates a random verb. Returns both key and value for the adjectives and nouns to adhere too. This one doesn't use and file ios as the list is still short.'''

	verbs = {
	
	"food":["eat", "bite", "chew", "munch", "cut", "lick"],
	"drink" : ["sip", "drink", "slurp"],
	"appliance": [ "sit on", "carry" , "break", "fix", "repair", "use", "touch" , "tap"],
	"clothes" : ["wear", "carry", "make", "hold", "put on"]
	}

	key = choice(list(verbs))
	return [str(key), choice(verbs.get(key, ""))]


