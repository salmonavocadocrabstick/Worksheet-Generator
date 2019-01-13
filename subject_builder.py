# Subject Builder Class
#
# Stephanie Leung (2019) - Worksheet Generator

from subject import *
from random import randint, choice, sample
import subject_list_names as name_list
import subject_list_pronouns as pronoun_list



class SubjectBuilder:
	def __init__(self, number_of_people):
		self.subjects = []
		self.number_of_people = number_of_people


class PronounBuilder(SubjectBuilder):
	def __init__(self, number_of_people=0):
		super().__init__(number_of_people)
		self.subjects.append(Pronoun(choice(pronoun_list.get_list())).get_name())
		if self.subjects[0] == "He" or  self.subjects[0] == "She" or self.subjects[0] == "It":
			number_of_people = 1 #Marking 

class NameBuilder(SubjectBuilder):
	def __init__(self, number_of_people):
		super().__init__(number_of_people)
		self._count = 0
		if number_of_people > 0:
			#2: x and y
			while self._count != number_of_people:
				self.subjects.append(Name(choice(name_list.get_list())).get_name())
				self._count += 1


# test = PronounBuilder()
# print(test.subjects[0])
# test1 = NameBuilder(2)
# print(test1.subjects[0])
# print(test1.subjects[1])