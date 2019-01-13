# Objects Builder
# 
# Stephanie Leung (2019)
from random import choice


class AbstractObject:

	@classmethod
	def get_noun(self):
		pass

	@classmethod
	def get_adj(self):
		pass


class Objects(AbstractObject):
	def __init__(self, item_type):
	# self.adj = adj
	# self.noun = noun
	self.item_type = item_type

	def get_type(self):
		return self.type


class AbstractObjectDecorator(AbstractObject):
	def __init__(self, decorated_obj):
		self.decorated_obj = decorated_obj


class Noun(AbstractObjectDecorator):
	def __init__(self, decorated_obj):
		AbstractObjectDecorator.__init__(self, decorated_obj)

	def get_noun(self):
		return noun_item  #!!!DEFINE THIS


class Adjective(AbstractObjectDecorator):
	def __init__(self, decorated_obj):
		AbstractObjectDecorator.__init__(self, decorated_obj)
		return adjective_item #!!!DEFINE THIS



# class ObjectBuilder:
# 	@classmethod
# 	def set_noun(self):
# 		pass

# 	@classmethod
# 	def set_adj(self):
# 		pass


# class NounBuilder(ObjectBuilder):
# 	def __init__(self, item_type):
# 		self.noun_obj = Objects(item_type)

# 	def set_noun(self):
# 		self.noun_object.noun = choice()


# class AdjectiveBuilder(ObjectBuilder):
# 	def __init__(self, item_type):
# 		self.adj_obj = Objects(item_type)

# 	def set_adj(self):
# 		self.adj_obj = Objects(item_type)

# class NounAndAdjBuilder(ObjectBuilder):
# 	def __init__(self):
# 		self.noun_and_adj_object = Objects()
# 	def set_noun(self):
# 		pass
# 	def set_adj(self):
# 		pass


