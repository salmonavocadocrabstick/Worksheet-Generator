# Templates for different types of sentences
# 
# Stephanie Leung
import sentence_element_builder as sentence_object
from copy import deepcopy
from random import randint
import wh_words as wh_word
import inflect
p = inflect.engine() #use to set grammar rules


# Takes in sentence object for further adjustments
class SentenceTemplate:

	def __init__(self, sentence):
		self.sentence = deepcopy(sentence)
		self.is_neg = False
		self.is_question = False
		self.ignore_do = False

	def set_tense(self):
		pass

	def process_s_obj(self, set_true = None):
		raise NotImplementedError

	def _process_nouns(self):
		self.sentence.set_noun(p.plural(self.sentence.get_noun(), self.sentence.get_num_nouns()))

	def _set_singular_verbs(self):
		'''Check number of subjects, change verb if necessary. (default verb is plural)'''
		if self.sentence.get_num_subj() == 1:
			verb = self.sentence.get_verb()
			#print(type(verb))
			self.sentence.set_verb(p.plural(verb))
		return self

	def _handle_there(self, pos_neg):
		self.sentence.set_verb(p.plural(pos_neg, self.sentence.get_num_nouns()))

		if self.sentence.get_num_nouns() == 1:
			article = p.an(self.sentence.get_noun())
			self.sentence.set_num_nouns(article[0])

		elif self.sentence.get_num_nouns() > 1 or self.sentence.get_num_nouns() == 0:
			self.sentence.set_num_nouns("any")


	def _modify_by_q_word(self): 
		#Careful: ONLY run this after deciding that the sentence is indeed a question.
		if self.sentence.get_is_q():
			if self.sentence.get_q_word() == "does":
				if self.sentence.get_num_subj() != 1:
					self.sentence.set_q_word("do") 	#They/I/You/We
					#self.set_q_word()
			elif self.sentence.get_q_word() == "there" :
				if self.sentence.get_verb():
					self._handle_there("is")
			self.is_question = True
		#return self

	def _roll_for_negative(self):
		#Careful: ONLY run this after confirming that this sentence is NOT a question.
		set_neg = randint(0,1)
		if set_neg:
			if self.sentence.get_q_word() == "does": # does not/ do not
				if self.sentence.get_num_subj() != 1:
					self.sentence.set_q_word("do not") 	#They/I/You/We
				else:
					self.sentence.set_q_word("does not") 
			elif self.sentence.get_q_word() == "can":	# cannot
				self.sentence.set_q_word("cannot") 

			elif self.sentence.get_q_word() == "there":
				self._handle_there("is not")
			self.is_neg = True


	def _handle_positive(self):
		if self.sentence.get_q_word() in ["do", "does"]:
			self.ignore_do = True

		if self.sentence.get_q_word() == "there":
			self.sentence.set_verb(p.plural("is", self.sentence.get_num_nouns()))

	def _add_bracket(self, word):
		return f"!({word})"


	def set_blank(self, target):
		raise "Subclass should implement!"

	def get_wrapped_sentence_obj(self):
		return self

	def get_mod_sentence_obj(self):
		return self.sentence

class FillInTheBlanks_Verb(SentenceTemplate):
	def __init__(self, sentence):
		super().__init__(sentence)

	def process_s_obj(self, set_true = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_true == None:
			set_true = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_true:
			# Only set true if a q word is found.
			if self.sentence.get_q_word():
				self.sentence.set_is_q(True)  
				self._modify_by_q_word()
		
		# Not a question type, roll to see if its positive / negative	
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		# Verb form, thus change "is/am/are" to "be"
		if self.sentence.get_verb() in ["are", "is", "is not", "are not"]:
			bracketed_word = self._add_bracket("be")
			self.sentence.set_verb(bracketed_word)
		else:
			bracketed_word = self._add_bracket(self.sentence.get_verb())
			self.sentence.set_verb(bracketed_word)

		self._process_nouns()
		return self

class FillInTheBlanks_Noun(SentenceTemplate):
	def __init__(self, sentence):
		super().__init__(sentence)

	def process_s_obj(self, set_true = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_true == None:
			set_true = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_true:
			# Only set true if a q word is found.
			if self.sentence.get_q_word():
				self.sentence.set_is_q(True)  
				self._modify_by_q_word()
				
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		if self.ignore_do or not self.sentence.get_q_word() :
			self._set_singular_verbs()	

		bracketed_word = self._add_bracket(self.sentence.get_noun())
		self.sentence.set_noun(bracketed_word)
		return self


class FullSentence(SentenceTemplate):
	def __init__(self, sentence):
		super().__init__(sentence)
		
	def process_s_obj(self, set_question = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_question == None:
			set_question = randint(0,1)

		# Rolled is question, now check if there's a q word at all
		if set_question:
			# Only set true if a q word is found.
			if not self.sentence.get_q_word():
				# Force a q word into the slot.
				while not self.sentence.get_q_word():
					word = wh_word.get_question_word()
					if word:
						break

				self.sentence.set_q_word(word)

			#if self.sentence.get_q_word():
			self.sentence.set_is_q(True)  
			self._modify_by_q_word()
				
		else:
			self._roll_for_negative()
			if not self.is_neg:
				self._handle_positive()

		if self.ignore_do or not self.sentence.get_q_word() :
			self._set_singular_verbs()	

		self._process_nouns()
		return self


