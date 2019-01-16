# Templates for different types of sentences
# 
# Stephanie Leung
import sentence_element_builder as sentence_object
from copy import deepcopy
import inflect
p = inflect.engine() #use to set grammar rules


# Takes in sentence object for further adjustments
class SentenceTemplate:

	def __init__(self, sentence):
		self.sentence = deepcopy(sentence)

	def set_tense(self):
		pass

	def set_question(self):
		pass

	def set_plural_nouns(self):
		if self.sentence.get_num_nouns() > 1:
			self.sentence.noun = p.plural(self.sentence.get_noun()[0])
		self.sentence.num_nouns = p.number_to_words(self.sentence.num_nouns) # 1/15/2019: Number of items limit 0-9 now. Grouping may need change if larger than 10.
		return self

	def set_plural_verbs(self):
		if self.sentence.get_num_subj() == 1:
			self.sentence.verb[1] = p.plural(self.sentence.get_verb()[1])
		return self

	def set_blank(self, target):
		raise "Subclass should implement!"

	def get_sentence(self):
		return self.sentence

class FillInTheBlanks_Verb(SentenceTemplate):
	def set_blank(self):
		if self.sentence.get_verb()[1]:
			self.sentence.verb[1]=(f"!({self.sentence.get_verb()[1]})")
			print(self.sentence.verb[1])
		return self


class FillInTheBlanks_Noun(SentenceTemplate):
	def set_blank(self):
		if self.sentence.get_noun():
			self.sentence.noun[0] = f"!({self.sentence.get_noun()})"
		return self

