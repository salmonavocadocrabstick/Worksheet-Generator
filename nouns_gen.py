

def get_noun_list(noun_bank):
	'''Returns a designated (pre-scraped) noun list as a long list'''
	with open(noun_bank, "r") as nouns:
		noun_list = nouns.read().split("\n")[:-2:]
	return noun_list
