# Objects - Decorator Pattern
# 
# Stephanie Leung (2019)
from random import choice, randint
import nouns_gen as nouns_gen
import adjective_gen as adj_gen


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
		#self.item_type = decorated_obj.get_type()

	def get_adj(self):
		if self.adj:
			return self.adj

class Quantity(AdjectiveDecorator):
 	def __init__(self, decorate_type):
 		AdjectiveDecorator.__init__(self, decorate_type)
 		self.adj = adj_gen.quantity_adj_generator(decorate_type)

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

	adj_type = randint(1,3)

	#if adj_type == 0:
	#	return Quantity(decorate_type).get_adj()
	if adj_type == 1:
		return Quality(decorate_type).get_adj()
	elif adj_type == 2:
		return Size(decorate_type).get_adj()
	elif adj_type == 3:
		return Color(decorate_type).get_adj()

def get_quantity_countable(decorate_type):
	return randint(0, 9)

def get_quantity_uncountable(decorate_type):
	return Quantity(decorate_type).get_adj()


def get_noun(decorate_type):
	return Noun(decorate_type).get_noun()


# test1 = Noun("food")
# print(test1.noun)
# print(set_adjective("food"))