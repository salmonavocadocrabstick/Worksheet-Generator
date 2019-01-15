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
		pass

	def get_sentence(self):
		return self.sentence


class FillInTheBlanks_Verb(SentenceTemplate):
	def set_blank(self):
		if self.sentence.get_verb()[1]:
			self.sentence.verb.append(f"({self.sentence.get_verb()[1]})")
			self.sentence.verb[1] = "____________________"
		return self


class FillInTheBlanks_Noun(SentenceTemplate):
	def set_blank(self):
		if self.sentence.get_noun():
			#noun = []
			#noun.append("____________________")
			noun[0] = f"({self.sentence.get_noun()})"
			self.sentence.noun = noun
		return self



# test = sentence_object.SentenceObjectBuilder().set_subj().set_verb().set_noun().set_quantity().set_adjective().get_sentence_obj()
# # print(f"{test.subj.subjects[0]} {test.verb[1]} {test.num_nouns} {test.adj} {test.noun}")

# # #test1 = deepcopy(test)


# FIBV = FillInTheBlanks_Verb(test).set_plural_nouns().set_blank().get_sentence()
# print(f"{FIBV.subj.subjects[0]} {FIBV.verb[1]} {FIBV.verb[2]} {FIBV.num_nouns} {FIBV.adj} {FIBV.noun}.")



# FIBN = FillInTheBlanks_Noun(test).set_plural_verbs().set_blank().get_sentence()
# print(f"{FIBN.subj.subjects[0]} {FIBN.verb[1]} {FIBN.num_nouns} {FIBN.adj} {FIBN.noun[0]} {FIBN.noun[1]}.")


# FIBN = FillInTheBlanks_Noun().set_plural_verbs(test)
# print(f"{test.subj.subjects[0]} {test.verb[1]} {test.num_nouns} {test.adj} {test.noun}")




