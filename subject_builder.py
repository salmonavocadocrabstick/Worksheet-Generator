# Subject Builder Class
#
# Stephanie Leung (2019) - Worksheet Generator

from subject import *
from random import randint, choice, sample
import subject_list_names as name_list
import subject_list_pronouns as pronoun_list



class SubjectBuilder:
	def __init__(self, num_subj):
		self.subjects = []
		self.num_subj = num_subj

	def get_num_subj(self):
		return self.num_subj


class PronounBuilder(SubjectBuilder):
	def __init__(self, num_subj=0):
		super().__init__(num_subj)
		self.subjects.append(Pronoun(choice(pronoun_list.get_list())).get_name())
		if self.subjects[0] == "he" or  self.subjects[0] == "she" or self.subjects[0] == "it":
			self.num_subj = 1 #Marking 

class NameBuilder(SubjectBuilder):
	def __init__(self, num_subj):
		super().__init__(num_subj)
		self._count = 0
		if num_subj > 0:
			#2: x and y
			while self._count != num_subj:
				self.subjects.append(Name(choice(name_list.get_list())).get_name())
				self._count += 1


# test = PronounBuilder()
# print(test.subjects[0])
# test1 = NameBuilder(2)
# print(test1.subjects[0])
# print(test1.subjects[1])