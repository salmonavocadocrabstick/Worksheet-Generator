# Subject class
#
# Stephanie Leung (2019) - Worksheet Generator

class Subject:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

class Pronoun(Subject):
	def __init__(self, name):
		super().__init__(name)


class Name(Subject):
	def __init__(self, name):
		super().__init__(name)
