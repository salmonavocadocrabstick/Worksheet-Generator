# Sentence Builder
#
# Stephanie Leung (2019)
import subject_builder as subj_bd
from random import randint, choice
import verbs_gen
import objects_gen

class Sentence:
	def __init__(self, subj="", verb="", adj="", noun="", q_word="", question="", keyword=""):
		self.subj = subj
		self.verb = verb
		self.adj = adj
		self.noun = noun
		self.q_word = q_word
		self.question = question
		self.keyword = keyword


class Builder:

	def get_result(self):
		pass

	@classmethod
	def set_subj_name(self):
		pass

	@classmethod
	def set_verb(self):
		pass

	@classmethod
	def set_adjective(self):
		pass

	def set_noun(self):
		pass

	def set_plural(self):
		pass

	def set_question_word(self):
		pass

	def set_question(self, value):
		pass

	def set_statement(self, value):
		pass

	def set_fill_in_blanks(self, value):
		pass

	def set_tenses(self, value):
		pass

	def set_keywords(self):
		pass


class SentenceBuilder(Builder):
	def __init__(self):
		self.sentence = Sentence()

	def set_subj_name(self):
		roll_dice = randint(1, 49)
		if roll_dice % 2 == 0:
			self.sentence.subj = subj_bd.PronounBuilder()
		else:
			number_of_people = randint(1,3)	#Unlikely needing more than 3 people, like, ever...
			self.sentence.subj = subj_bd.NameBuilder(number_of_people)
		return self

	def set_verb(self):
		self.sentence.verb = verbs_gen.verb()
		return self

	def set_noun(self):
		if self.sentence.verb:
			self.sentence.noun = objects_gen.phrase_generate(self.sentence.verb[0])
		return self

	def set_adjective(self):
		pass


class FillInTheBlanksNounsBuilder():
	def make_FIB():
		return SentenceBuilder


sentenceBlder = SentenceBuilder().set_subj_name().set_verb().set_noun()
test = sentenceBlder.sentence

print(f"{test.subj.subjects[0]} {test.verb[1]} {test.noun}")

# print(test.sentence.subj.subjects[1])
# print(test.sentence.subj.number_of_people)
# print(test.sentence.verb[1])
# print(test.sentence.noun)