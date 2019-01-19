# Objects - Decorator Pattern
# 
# Stephanie Leung (2019)
from random import randint
from numpy.random import choice
import nouns_gen as nouns_gen
import adjective_gen as adj_gen

DEBUG = False

class AbstractObject:
	pass	#Simplifying for now but  may need to add in more later.

class Noun(AbstractObject):
	def __init__(self, item_type):
		self.item_type = item_type
		self.noun = nouns_gen.noun_generate(self.item_type) 
	def get_noun(self):
		return self.noun

class AdjectiveDecorator(AbstractObject):
	def __init__(self, decorate_type):
		self.decorate_type = decorate_type

	def get_adj(self):
		if self.adj:
			return self.adj

class State(AdjectiveDecorator):
 	def __init__(self, decorate_type):
 		AdjectiveDecorator.__init__(self, decorate_type)
 		self.adj = adj_gen.state_adj_generator(decorate_type)

class Quality(AdjectiveDecorator):
	def __init__(self, decorate_type):
		AdjectiveDecorator.__init__(self, decorate_type)
		self.adj = adj_gen.quality_adj_generator(decorate_type)

class Size(AdjectiveDecorator):
	def __init__(self, decorate_type):
		AdjectiveDecorator.__init__(self, decorate_type)
		self.adj = adj_gen.size_adj_generator(decorate_type)

class Color(AdjectiveDecorator):
	def __init__(self, decorate_type):
		AdjectiveDecorator.__init__(self, decorate_type)
		self.adj = adj_gen.color_adj_generator(decorate_type)


def get_adjective(decorate_type):

	#adj_type = randint(1,3)
	# Color = 1
	# Quality = 2
	# Size = 3
	# State = 4
	if decorate_type in ["food", "drink", "appliance", "clothes"]:
		# all adjectives are fine
		adj_type = choice([1,2,3,4], p=[0.1, 0.2, 0.35, 0.35])

	elif decorate_type == "activities":
		# quality and size only
		adj_type = choice([2,3], p=[0.65, 0.35])
		
	elif decorate_type == "raw_mats":
		#color, quality only
		adj_type = choice([3,1], p=[0.35, 0.65])


	if DEBUG:
		print(f"{decorate_type} {adj_type}")

	if adj_type == 1:
		return Color(decorate_type).get_adj()
	elif adj_type == 2:
		return Quality(decorate_type).get_adj()
	elif adj_type == 3:
		return Size(decorate_type).get_adj()
	elif adj_type == 4:
		return State(decorate_type).get_adj()


def get_quantity_countable(decorate_type):
	return randint(1, 8)
	# 1/19 : Note on uncountable nouns, may need to come back and fix.
	# 1/19: Implementing temp fix on uncountable nouns (drinks, raw mats)

def get_quantity_uncountable(decorate_type):
	return Quantity(decorate_type).get_adj()

def get_noun(decorate_type):
	return Noun(decorate_type).get_noun()


# test1 = Noun("food")
# print(test1.noun)
# print(set_adjective("food"))