# Subject Builder Class
#
# Stephanie Leung (2019) - Worksheet Generator

from subject import *
from random import randint, choice, sample
import subject_list_names as name_list
import subject_list_pronouns as pronoun_list



class SubjectBuilder:

	#Class Attribute
	_pronoun = 0
	_name = 1
	_count = 0

	def __init__(self, subj_type, number_of_people = 0):
		self.subjects = []
		self.number_of_people = number_of_people

		if subj_type == SubjectBuilder._pronoun:
			self.subjects.append(Pronoun(choice(pronoun_list.get_list())))

		elif subj_type == SubjectBuilder._name:

			if number_of_people > 0:
				#2: x and y
					while SubjectBuilder._count != number_of_people:
						self.subjects.append(Name(choice(name_list.get_list())))
						SubjectBuilder._count += 1


# pronoun = 0
# name = 1
# test1 = SubjectBuilder(pronoun)
# print(test1.subjects[0])

# test2 = SubjectBuilder(name, 3)
# print(test2.subjects[0].name)
# print(test2.subjects[1].name)
# print(test2.subjects[2].name)
