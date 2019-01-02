from random import choice, randint


verbs = {
	
	"food":["eat", "bite", "chew", "munch"],
	"drink" : ["sip", "drink"],
	"appliance": [ "sit on", "carry" , "break", "fix", "repair", "use", "touch" , "tap"],
	"clothes" : ["wear", "carry", "make", "hold", "put on"]
}


def verb():
	key = choice(list(verbs))
	#return { str(key) : choice(verbs.get(key, ""))}
	return [str(key), choice(verbs.get(key, ""))]
	# f"{choice(verbs)}"

