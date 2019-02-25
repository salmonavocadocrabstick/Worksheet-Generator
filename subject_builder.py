# Subject Builder Class
#
# Stephanie Leung (2019) - Worksheet Generator

#from subject import *
from random import randint, choice
import names_and_pronoun_list as np_list


class Subject:
	def __init__(self, num_subj):
		self.subjects = []
		self.num_subj = num_subj

	def get_num_subj(self):
		return self.num_subj


class Pronoun(Subject):
	'''Subclass of Subject. Generates pronouns for sentence object. Default sets num_subj to 0. 
	Also auto switches num_subj to 1 if the pronoun is he/she/it '''
	def __init__(self, num_subj=0):
		super().__init__(num_subj)
		self.subjects.append(choice(np_list.get_pronoun_list()))
		if self.subjects[0] == "he" or  self.subjects[0] == "she" or self.subjects[0] == "it":
			self.num_subj = 1 #Marking 

class Name(Subject):
	'''Subclass of Subject. Generates names for sentence object. Pulls name from a different python file.
	Has a count_ variable that is used to keep track of the number of names generated. Is not for external use'''
	def __init__(self, num_subj):
		super().__init__(num_subj)
		self._count = 0
		if num_subj > 0:
			#2: x and y
			while self._count < num_subj:
				self.subjects.append(choice(np_list.get_name_list()))
				if self._count + 1 == num_subj-1 :
					add_I = randint(0, 1)
					# 50/50 to turn the last person as "I"
					if add_I :
						self.subjects.append("I")
						self._count += 1
						#return None

				self._count += 1


# test = Pronoun()
# print(test.subjects[0])
# test1 = Name(2)
# print(test1.subjects[0])
# print(test1.subjects[1])