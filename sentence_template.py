# Templates for different types of sentences
# 
# Stephanie Leung
import sentence_element_builder as sentence_object
from copy import deepcopy
from random import randint
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

	def set_question(self, set_true = None):
		'''Checks if the object is set as a question. If no default setting, roll for it
		Sorts the job to the next function if needed'''
		if set_true == None:
			set_true = randint(0,1)

		if set_true:
			if self.sentence.get_q_word():
				self.sentence.set_is_q(True)  #Only true if there was a word.
				self._modify_by_q_word()
				
		else:
			self._set_negative()
		return self


	# def set_plural_nouns(self):
	# 	if self.sentence.get_num_nouns() > 1:
	# 		self.sentence.noun = p.plural(self.sentence.get_noun()[0])
	# 	self.sentence.num_nouns = p.number_to_words(self.sentence.num_nouns) # 1/15/2019: Number of items limit 0-9 now. Grouping may need change if larger than 10.
	# 	return self

	def set_plural_verbs(self):
		'''Check number of subjects, change verb if necessary. (default verb is plural)'''
		if self.sentence.get_num_subj() == 1:
			verb = self.sentence.get_verb()
			print(type(verb))
			self.sentence.set_verb(p.plural(verb))
		return self

	def _modify_by_q_word(self): 
		#Careful: ONLY run this after deciding that the sentence is indeed a question.
		if self.sentence.get_is_q():
			if self.sentence.get_q_word() == "does":
				if self.sentence.get_num_subj != 1:
					self.sentence.set_q_word("do") 	#They/I/You/We
					#self.set_q_word()
			elif self.sentence.get_q_word() == "there" :
				if self.sentence.get_verb() and self.sentence.get_num_nouns() == 1:
					self.sentence.set_verb("is")
				else:
					self.sentence.set_verb("are")
			self.is_question = True
		#return self

	def _set_negative(self):
		#Careful: ONLY run this after confirming that this sentence is NOT a question.
		set_neg = randint(0,1)
		if set_neg:
			if self.sentence.get_q_word() == "does": # does not/ do not
				if self.sentence.get_num_subj != 1:
					self.sentence.set_q_word("do not") 	#They/I/You/We
				else:
					self.sentence.set_q_word("does not") 
			elif self.sentence.get_q_word() == "can":	# cannot
				self.sentence.set_q_word("cannot") 

			elif self.sentence.get_q_word() == "there":
				self.sentence.set_verb(str(self.sentence.get_verb()) + " not")
			#self.is_neg = True

		else: #Positive statement, ignore do or does
			if self.sentence.get_q_word() in ["do", "does"]:
				self.ignore_do = True
		return self


	def set_blank(self, target):
		raise "Subclass should implement!"

	def get_wrapped_sentence_obj(self):
		return self

	def get_mod_sentence_obj(self):
		return self.sentence

# class FillInTheBlanks_Verb(SentenceTemplate):
# 	def set_blank(self):
# 		if self.sentence.get_verb()[0]:
# 			self.sentence.verb[0]=(f"!({self.sentence.get_verb()[0]})")
# 		return self

# class FillInTheBlanks_Noun(SentenceTemplate):
# 	def set_blank(self):
# 		if self.sentence.get_noun():
# 			self.sentence.noun[0] = f"!({self.sentence.get_noun()})"
# 		return self


# class FillInTheBlanks_YesNoQ(SentenceTemplate):
# 	def set_blank(self):
# 		if self.sentence.get_q_word():
# 			self.sentence.q_word = f"!({self.sentence.get_q_word()})"
# 		return self

# Notes: For the verbs, come back and implement inflect join() function so that multiple verbs can be used later
