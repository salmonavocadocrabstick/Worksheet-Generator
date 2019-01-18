

# This class constructs the sentences with the given words
# Does not add any grammar rules
# Checks what words are available 
# and generates sentences according to the words

# Again, it DOES NOT ADD ANY GRAMMAR RULES YOU CRAZY OLD BAT

import sentence_element_builder as sentence_object
import sentence_grammar as sentence_grammar
from random import shuffle
import inflect
p = inflect.engine()

DEBUG = False


class SentenceConstruction():
	def __init__(self):
		self.part_a = ""
		self.part_b = ""
		self.is_split = False
	
	def get_full_sentence(self):
		if self.full_sentence:
			self.full_sentence = self.full_sentence[0].upper() + self.full_sentence[1:]
			return self.full_sentence

	def get_part_a(self):
		if "!(" in self.full_sentence and not self.is_split:
			self.part_a, self.part_b = self.full_sentence.split("!")
			self.is_split = True
		if len(self.part_a) > 0:
			self.part_a = self.part_a[0].upper() + self.part_a[1:]
		return self.part_a

	def get_part_b(self):
		if "!(" in self.full_sentence and not self.is_split:
			self.part_a, self.part_b = self.full_sentence.split("!")
			self.is_split = True
			
		if len(self.part_b) > 0:
			self.part_b = self.part_b[0].upper() + self.part_b[1:]
		return self.part_b

	def get_jumboed_sentence(self):
		if "!(" in self.full_sentence:
			raise "You cannot request for Sentence Rearragement targets with fill in the blanks objects"
			return None

		sentence_list = self.full_sentence.split(" ")
		shuffle(sentence_list)
		return sentence_list

class QuestionConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		super().__init__()
		if wrapped.sentence.get_q_word() in ["do", "does", "can"]:
			if DEBUG:
				print("Question - 4 ")
			self.full_sentence =  f"{wrapped.sentence.get_q_word()} {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {wrapped.sentence.get_num_nouns()} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}? "
		elif wrapped.sentence.get_q_word() == "there":
			if DEBUG:
				print("Question - 5 ")
			self.full_sentence =  f"{wrapped.sentence.get_verb()} {wrapped.sentence.get_q_word()} {wrapped.sentence.get_num_nouns()} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}?"

class StatementConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		super().__init__()
		if wrapped.sentence.get_q_word() == "there":
			# There are ..
			counter = p.number_to_words(wrapped.sentence.get_num_nouns())
			if counter == "zero":
				counter = wrapped.sentence.get_num_nouns()
			if DEBUG:
				print("Statement - 3 ")
			self.full_sentence = f"{wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {counter} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."
		else:
			#Something's a bit wonky with the logic...
			#Maybe there's a better way to combine counter + adj + noun with inflect
			if wrapped.ignore_do:
				if DEBUG:
					print("Statement - 1 ")
				# He eats 5 potatoes
				self.full_sentence = f"{wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."
			elif wrapped.sentence.get_q_word():
				if DEBUG:
					print("Statement - 2a ")
				# He can eat 5 potatoes
				self.full_sentence = f"{wrapped.sentence.get_subj()} {wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."
			else:
				if DEBUG:
					print("Statement - 2b ")
				# He eats 5 potatoes
				self.full_sentence = f"{wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."


def generate_sentence_by_type(sentence_object):
	if sentence_object.is_question:
		return QuestionConstruction(sentence_object.get_wrapped_sentence_obj())

	else:
		return StatementConstruction(sentence_object.get_wrapped_sentence_obj())




# s_obj = sentence_object.get_s_obj()
# mo_obj = sentence_grammar.FIBV_sentence_obj(s_obj)
# #print(sort_modified_s_obj(mo_obj))
# mo_obj2 = sentence_grammar.FIBN_sentence_obj(s_obj)
# #print(sort_modified_s_obj(mo_obj2))
# mo_obj3 = sentence_grammar.FS_sentence_obj(s_obj)
# #print(sort_modified_s_obj(mo_obj3))
# mo_obj4 = sentence_grammar.Q_sentence_obj(s_obj)
# #print(sort_modified_s_obj(mo_obj4))