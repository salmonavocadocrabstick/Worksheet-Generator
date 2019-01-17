# Sentence Builder
#
# Stephanie Leung (2019)
import subject_builder as subj_bd
import object_decorator as obj_dc
import wh_words as wh_word
import inflect
from copy import deepcopy
from random import randint, choice
import verbs_gen

p = inflect.engine()

class SentenceObject:
	def __init__(self, subj="", verb="", adj="", noun="", q_word=""):
		self.subj = subj
		self.num_subj = 0
		self.v_type = None
		self.verb = verb
		self.adj = adj
		self.num_nouns = 0
		self.noun = noun
		self.q_word = q_word
		self.is_q = False



	def get_noun(self):
		noun_copy = deepcopy(self.noun)
		return p.join(noun_copy)

	def set_noun(self, noun):
		self.noun = noun

	def get_verb(self):
		verb_copy = deepcopy(self.verb)
		return p.join(verb_copy)

	def set_verb(self, verb):
		self.verb = [verb]

	def get_num_nouns(self):
		return self.num_nouns

	def set_num_nouns(self, num):
		self.num_nouns = num

	def get_num_subj(self):
		return self.num_subj

	def set_num_subj(self, num):
		self.num_subj = num

	def get_q_word(self):
		'''String type, single question word'''
		return self.q_word

	def set_q_word(self, word):
		'''Sets a string - single question word'''
		self.q_word = word

	def get_is_q(self):
		return self.is_q

	def set_is_q(self, true_or_false):
		self.is_q = true_or_false


	def get_subj(self):
		#self.subj.subjects = ["Lisa", "Bill", "Bob"]
		subj_copy = deepcopy(self.subj.subjects)
		return p.join(subj_copy)

	def get_v_type(self):
		return self.v_type

	#def set_is_neg(self, status):
	#	self.is_neg = status


class SentenceObjectBuilder():
	def __init__(self):
		self.sentence = SentenceObject()

	def gen_subj(self):
		roll_dice = randint(1, 49)
		if roll_dice % 2 == 0:
			self.sentence.subj = subj_bd.PronounBuilder()
			self.sentence.num_subj = self.sentence.subj.get_num_subj()
		else:
			self.sentence.num_subj = randint(1,3)	#Unlikely needing more than 3 people, like, ever...
			self.sentence.subj = subj_bd.NameBuilder(self.sentence.num_subj)
		return self

	def gen_verb(self):
		verb_pair = verbs_gen.verb()
		self.sentence.v_type = verb_pair[0]
		self.sentence.verb = verb_pair[1:]
		return self

	def gen_noun(self):
		if self.sentence.verb:
			self.sentence.noun = obj_dc.get_noun(self.sentence.v_type)
		return self

	def gen_quantity(self):
		if self.sentence.verb:
			self.sentence.num_nouns = obj_dc.get_quantity_countable(self.sentence.v_type)
		return self

	def gen_adjective(self):
		if self.sentence.verb:
			if self.sentence.noun:
				self.sentence.adj = obj_dc.get_adjective(self.sentence.v_type)
		return self

	def gen_question_word(self):
		self.sentence.q_word = wh_word.get_question_word()
		return self

	def get_sentence_object(self):
		return self.sentence

	
def get_s_obj():
		#s_obj = sentence_object.SentenceObjectBuilder().gen_subj().gen_verb().gen_noun().gen_quantity().gen_adjective().get_sentence_obj()
		return SentenceObjectBuilder().gen_subj().gen_verb().gen_noun().gen_quantity().gen_adjective().gen_question_word().get_sentence_object()



# sentenceBlder = SentenceObjectBuilder().gen_subj().gen_verb().gen_noun().gen_quantity().gen_adjective()
# test = sentenceBlder.sentence

# print(type(sentenceBlder))
# print(type(test))


# print(f"{test.subj.subjects[0]} {test.verb[1]} {test.num_nouns} {test.adj} {test.noun}")

