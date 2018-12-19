from random import choice, randint

verbs = 	[
				"wear",
				"eat",
				"drink",
				"make",
				"break",
				"touch",
				"carry",
				"hold",
				"tap"
			]

def verb():
	return f"{choice(verbs)}"