# Templates for different types of sentences
# 
# Stephanie Leung
import sentence_obj_builder as s_obj
from copy import deepcopy
from random import randint, choice
import wh_words as wh_word
import inflect
import pres_keywords_gen as pres_keyword
p = inflect.engine() #use to set grammar rules


########################################################################
#
#	1/19/2018: Supports Can / Does / Do / There sentences for now
#		- Present tense is functional
#		- Implementing Past tense soon.
#####


# Takes in sentence object for further adjustments
class SentenceTemplate:

	def __init__(self, s_obj, tense="present"):
		self.s_obj = deepcopy(s_obj)
		self.is_neg = False
		self.is_question = False
		self.ignore_do = False
		self.tense = tense
		self.keyword = ""

	def get_keyword(self):
		if self.keyword:
			return self.keyword

	def set_tense(self):
		'''To be implemented. Planning to make Past Tense/Future tense practices'''
		pass

	def _gen_keyword_by_tense(self):
		if self.tense == "present":
			self.keyword = pres_keyword.present_tense_keyword()

	def process_s_obj(self, set_true = None):
		raise NotImplementedError

	def _handle_uncountable_nouns(self):
		'''check if nouns are uncountable'''
		# Two conditions for now
		# 1) Is a drink
		# 2) Matches the items on the uncountable list.
		#if self.s_obj.get_v_type() in ["drink", "raw_mats"]:
		drink_counters = ["cup of ", "bottle of ", "jar of "]
		raw_mats_counters = ["box of ", "cup of ", "bowl of ", "pile of "]

		if self.s_obj.get_v_type() == "drink":
			#print("DRINK FOUND, uncountable!")
			noun_with_counter = choice(drink_counters) + self.s_obj.get_noun()
			self.s_obj.set_noun(noun_with_counter)
			#print(self.s_obj.get_noun())

		elif self.s_obj.get_v_type() == "raw_mats":
			#print("RAW MATT FOUND!")
			noun_with_counter = choice(raw_mats_counters) + self.s_obj.get_noun()
			self.s_obj.set_noun(noun_with_counter)
			#print(self.s_obj.get_noun())


	def _process_nouns(self):
		'''Pluralize/Singularize Nouns. Always run this before running _process_number()'''
		if self.s_obj.get_v_type() in ["drink", "raw_mats"]:
			self._handle_uncountable_nouns()

		self.s_obj.set_noun(p.plural(self.s_obj.get_noun(), self.s_obj.get_num_nouns()))

	def _set_singular_verbs(self):
		'''Check number of subjects, change verb if necessary. (default verb is plural)'''
		if self.s_obj.get_num_subj() == 1:
			verb = self.s_obj.get_verb()
			#print(type(verb))
			self.s_obj.set_verb(p.plural(verb))
		return self

	def _handle_be(self, verb):
		# Be - Is / Are
		# Note: When implementing "I am", will need to come back and revise.
		self.s_obj.set_verb(p.plural(verb, self.s_obj.get_num_nouns()))


	def _modify_by_q_word(self): 
		#Careful: ONLY run this after deciding that the s_obj is indeed a question.
		if self.s_obj.get_is_q():
			if self.s_obj.get_q_word() == "does":
				if self.s_obj.get_num_subj() != 1:
					self.s_obj.set_q_word("do") 	#They/I/You/We
					#self.set_q_word()
			elif self.s_obj.get_q_word() == "there" :
				if self.s_obj.get_verb():
					self._handle_be("is")
			self.is_question = True

	def _roll_for_negative(self):
		#Careful: ONLY run this after confirming that this s_obj is NOT a question.
		set_neg = randint(0,1)
		if set_neg:
			if self.s_obj.get_q_word() == "does": # does not/ do not
				if self.s_obj.get_num_subj() != 1:
					self.s_obj.set_q_word("do not") 	#They/I/You/We
				else:
					self.s_obj.set_q_word("does not") 
			elif self.s_obj.get_q_word() == "can":	# cannot
				self.s_obj.set_q_word("cannot") 

			elif self.s_obj.get_q_word() == "there":
				self._handle_be("is not")
			self.is_neg = True


	def _handle_positive(self):
		if self.s_obj.get_q_word() in ["do", "does"]:
			self.ignore_do = True

		if self.s_obj.get_q_word() == "there":
			self.s_obj.set_verb(p.plural("is", self.s_obj.get_num_nouns()))

	def _process_number(self):
		# Only call this after the s_obj has decided as a question or statement.
		# Only call this after pluralizing nouns		
		if self.s_obj.get_num_nouns() == 0:
			#Yes, 0
			self.s_obj.set_num_nouns("any")
		else:
			#No, not 0
			if self.s_obj.get_num_nouns() > 1:
				# Yes, greater than 1 noun
				if self.is_question:
					# Are there any... Can you eat any....
					self.s_obj.set_num_nouns("any")
				else:
					# There are 5 angry dogs | You can eat 5 angry boxes
					self.s_obj.set_num_nouns(p.number_to_words(self.s_obj.get_num_nouns()))
			else:
				# No, equals 1.
				# There is a.... There is an... Can you eat a....
				article = p.an(self.s_obj.get_noun())
				self.s_obj.set_num_nouns(article[0])

	def _add_bracket(self, word):
		'''Marks target word for fill in the blanks. Only use for fill in the blank type questions.'''
		return f"!({word})"


	def set_blank(self, target):
		raise "Subclass should implement!"

	def get_wrapped_sentence_obj(self):
		return self

	#def get_mod_s_obj_obj(self):
	#	return self.s_obj

class FillInTheBlanks_Verb(SentenceTemplate):
	'''Generates objects for sentences like : I can _______ (eat) a potatoe.'''
	def __init__(self, s_obj):
		super().__init__(s_obj)

	def process_s_obj(self, set_true = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_true == None:
			set_true = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_true:
			# Only set true if a q word is found.
			if self.s_obj.get_q_word():
				self.s_obj.set_is_q(True)  
				self._modify_by_q_word()
		
		# Not a question type, roll to see if its positive / negative	
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		# Verb form, thus change "is/am/are" to "be"
		if self.s_obj.get_verb() in ["are", "is", "is not", "are not"]:
			bracketed_word = self._add_bracket("be")
			self.s_obj.set_verb(bracketed_word)
		else:
			bracketed_word = self._add_bracket(self.s_obj.get_verb())
			self.s_obj.set_verb(bracketed_word)

		self._process_nouns()
		self._process_number()
		self._gen_keyword_by_tense()
		return self

class FillInTheBlanks_Noun(SentenceTemplate):
	'''Generates objects for sentences like : I eat five ______ (potatoe).'''
	def __init__(self, s_obj):
		super().__init__(s_obj)

	def process_s_obj(self, set_true = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_true == None:
			set_true = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_true:
			# Only set true if a q word is found.
			if self.s_obj.get_q_word():
				self.s_obj.set_is_q(True)  
				self._modify_by_q_word()
				
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		if self.ignore_do or not self.s_obj.get_q_word() :
			self._set_singular_verbs()	

		bracketed_word = self._add_bracket(self.s_obj.get_noun())
		self.s_obj.set_noun(bracketed_word)

		self._process_number()
		self._gen_keyword_by_tense()
		return self


class FullSentence(SentenceTemplate):
	'''Generates objects for sentences like : I can eat five potatoes.
	Mainly used for rearranging sentences / answering questions. '''
	def __init__(self, s_obj):
		super().__init__(s_obj)
		
	def process_s_obj(self, set_question = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_question == None:
			set_question = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_question:
			# Only set true if a q word is found.
			if not self.s_obj.get_q_word():
				# Force a q word into the slot.
				while not self.s_obj.get_q_word():
					word = wh_word.get_question_word()
					if word:
						break

				self.s_obj.set_q_word(word)

			self.s_obj.set_is_q(True)  
			self._modify_by_q_word()
				
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		if self.ignore_do or not self.s_obj.get_q_word() :
			self._set_singular_verbs()	

		self._process_nouns()
		self._process_number()
		self._gen_keyword_by_tense()
		return self


# For other scripts to call.
def FIBV_sentence_obj(s_obj):
	return FillInTheBlanks_Verb(s_obj).process_s_obj().get_wrapped_sentence_obj()

def FIBN_sentence_obj(s_obj):
	return FillInTheBlanks_Noun(s_obj).process_s_obj().get_wrapped_sentence_obj()

def FS_sentence_obj(s_obj):
	return FullSentence(s_obj).process_s_obj().get_wrapped_sentence_obj()

def Q_sentence_obj(s_obj):
	return FullSentence(s_obj).process_s_obj(set_question=True).get_wrapped_sentence_obj()

# To be implemented soon: 
# def M_sentence_obj(s_obj):
# 	return FullSentence(s_obj).process_s_obj(set_mistakes=True).get_wrapped_sentence_obj()
