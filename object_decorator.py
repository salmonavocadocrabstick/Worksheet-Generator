# Objects - Decorator Pattern
# 
# Stephanie Leung (2019)
from random import choice
import nouns_gen as nouns_gen
import adjective_gen as adj_gen


class AbstractObject:
	def get_type(self):
		if self.item_type:
			return self.item_type

class Noun(AbstractObject):
	def __init__(self, item_type):
		self.item_type = item_type
		self.noun = nouns_gen.noun_generate(self.item_type) 

	# def get_noun(self):
	# 	return 

class AdjectiveDecorator(AbstractObject):
	def __init__(self, decorated_obj, item_type):
		self.decorated_obj = decorated_obj
		self.item_type = item_type

	def get_adj(self):
		pass


class Quantity(AdjectiveDecorator):
	def __init__(self, decorated_obj):
		AdjectiveDecorator.__init__(self, decorated_obj)

	def get_adj(self):
		return adjective_item #!!!DEFINE THIS


class Quality(AdjectiveDecorator):
	def __init__(self, decorated_obj):
		AdjectiveDecorator.__init__(self, decorated_obj)

	def get_adj(self):
		return adjective_item #!!!DEFINE THIS


class Size(AdjectiveDecorator):
	def __init__(self, decorated_obj):
		AdjectiveDecorator.__init__(self, decorated_obj)

	def get_adj(self):
		return adjective_item #!!!DEFINE THIS

class Color(AdjectiveDecorator):
	def __init__(self, decorated_obj, item_type):
		AdjectiveDecorator.__init__(self, decorated_obj, item_type)

	def get_adj(self):
		return adj_gen.color_adj_generator(self.item_type)


# test1 = Noun("food")
# print(test1.noun)

# adj1 = Color(test1, test1.get_type())
# print(adj1.get_adj() + test1.noun)
