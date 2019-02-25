# Sentence Builder
#
# Stephanie Leung (2019)
import subject_builder as subj_bd
import object_decorator as obj_dc
import wh_words as wh_word
import verbs_gen

import inflect
import numpy.random

from copy import deepcopy
from random import randint, choice


p = inflect.engine()

class SentenceObject:
	'''Sentence Object Base; Contains subject, number of subjects, verb type identifier, 
	verb, adjective, noun counters, question word, tenses'''
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
		self.tense = "present"


	def get_noun(self):
		'''Returns a copy of the noun'''
		noun_copy = deepcopy(self.noun)
		return p.join(noun_copy)

	def set_noun(self, noun):
		'''Sets noun'''
		self.noun = [noun]

	def get_verb(self):
		'''Returns a copy of the verb'''
		verb_copy = deepcopy(self.verb)
		return p.join(verb_copy)

	def set_verb(self, verb):
		'''Sets verb'''
		self.verb = [verb]

	def get_num_nouns(self):
		'''Gets counter of nouns'''
		return self.num_nouns

	def set_num_nouns(self, num):
		'''Sets number of nouns'''
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

	def get_adj(self):
		return self.adj

	def get_subj(self):
		'''Returns a copy of the subject'''
		if self.subj.subjects:
			subj_copy = deepcopy(self.subj.subjects)
			return p.join(subj_copy)
		else:
			raise AttributeError("Subject is not generated yet. Could not get subject")

	def get_v_type(self):
		return self.v_type



class SentenceObjectBuilder():
	def __init__(self):
		'''Creates instance of sentence object'''
		self.sentence = SentenceObject()

	def gen_subj(self):
		'''Generates subject by rolling a dice. Note: subject cap at 3 people'''
		roll_dice = randint(1, 49)
		if roll_dice % 2 == 0:
			#Make pronouns
			self.sentence.subj = subj_bd.Pronoun()
			self.sentence.num_subj = self.sentence.subj.get_num_subj()
		else:
			# use names
			#self.sentence.num_subj = randint(1,3)	#Unlikely needing more than 3 people, like, ever...
			self.sentence.num_subj = numpy.random.choice(4, 1, p=[0, 0.7, 0.25, 0.05])
			self.sentence.subj = subj_bd.Name(self.sentence.num_subj)

		return self

	def gen_verb(self):
		'''Generates verbs. Takes the verb's key and marks it to the sentence's verb type as well for later usages '''
		verb_pair = verbs_gen.verb()
		self.sentence.v_type = verb_pair[0]	#Type of verb is important for choosing nouns later on.
		self.sentence.verb = verb_pair[1:]
		return self

	def gen_noun(self):
		'''Generates a noun with a given verb key. Do not use without verb key.'''
		if self.sentence.verb:
			self.sentence.noun = obj_dc.get_noun(self.sentence.v_type)
		else:
			raise Exception("No verb key found. Could not generate noun.")
		return self

	def gen_quantity(self):
		'''Generates a counter with a given verb key. Do not use without verb key.'''
		if self.sentence.verb:
			self.sentence.num_nouns = obj_dc.get_quantity_countable(self.sentence.v_type)
		else:
			raise Exception("No verb key found. Could not generate quantity.")
		return self

	def gen_adjective(self):
		'''Generates a counter with a given verb key. Do not use without verb key.'''
		if self.sentence.verb:
			if self.sentence.noun:
				self.sentence.adj = obj_dc.get_adjective(self.sentence.v_type)
		else:
			raise Exception("No verb key found. Could not generate adjectives.")
		return self

	def gen_question_word(self):
		self.sentence.q_word = wh_word.get_question_word()
		return self

	def get_sentence_object(self):
		'''Returns the entire sentence object'''
		return self.sentence

	
def get_s_obj():
	'''Returns a sentence object. Doesn't care about grammar what not. Just plain'o words'''
	return SentenceObjectBuilder().gen_subj().gen_verb().gen_noun().gen_quantity().gen_adjective().gen_question_word().get_sentence_object()


