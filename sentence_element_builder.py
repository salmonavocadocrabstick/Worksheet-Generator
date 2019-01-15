# Sentence Builder
#
# Stephanie Leung (2019)
import subject_builder as subj_bd
import object_decorator as obj_dc
from random import randint, choice
import verbs_gen


class SentenceObject:
	def __init__(self, subj="", verb="", adj="", noun="", q_word=""):
		self.subj = subj
		self.num_subj = 0
		self.verb = verb
		self.adj = adj
		self.num_nouns = 0
		self.noun = noun
		self.q_word = q_word
		#self.keyword = keyword

	def get_noun(self):
		return self.noun

	def get_verb(self):
		return self.verb

	def get_num_nouns(self):
		return self.num_nouns

	def get_num_subj(self):
		return self.num_subj


class SentenceObjectBuilder():
	def __init__(self):
		self.sentence = SentenceObject()

	def set_subj(self):
		roll_dice = randint(1, 49)
		if roll_dice % 2 == 0:
			self.sentence.subj = subj_bd.PronounBuilder()
			self.sentence.num_subj = self.sentence.subj.get_num_subj()
		else:
			self.sentence.num_subj = 1 #1/19: disabling for now randint(1,3)	#Unlikely needing more than 3 people, like, ever...
			self.sentence.subj = subj_bd.NameBuilder(self.sentence.num_subj)
		return self

	def set_verb(self):
		self.sentence.verb = verbs_gen.verb()
		return self

	def set_noun(self):
		if self.sentence.verb:
			self.sentence.noun = obj_dc.get_noun(self.sentence.verb[0])
		return self

	def set_quantity(self):
		if self.sentence.verb:
			self.sentence.num_nouns = obj_dc.get_quantity_countable(self.sentence.verb[0])
		return self

	def set_adjective(self):
		if self.sentence.verb:
			if self.sentence.noun:
				self.sentence.adj = obj_dc.get_adjective(self.sentence.verb[0])
		return self

	def get_sentence_obj(self):
		return self.sentence



# sentenceBlder = SentenceObjectBuilder().set_subj().set_verb().set_noun().set_quantity().set_adjective()
# test = sentenceBlder.sentence

# print(type(sentenceBlder))
# print(type(test))


# print(f"{test.subj.subjects[0]} {test.verb[1]} {test.num_nouns} {test.adj} {test.noun}")

