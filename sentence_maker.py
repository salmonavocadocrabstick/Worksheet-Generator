

# This class constructs the sentences with the given words
# Does not add any grammar rules
# Checks what words are available 
# and generates sentences according to the words

# Again, it DOES NOT ADD ANY GRAMMAR RULES YOU CRAZY OLD BAT

import sentence_element_builder as sentence_object
import sentence_grammar as sentence_grammar
import inflect
p = inflect.engine()


class SentenceConstruction():
	def __init__(self):
		self.halves = None
	
	def make_full_sentence(self):
		if self.full_sentence:
			return self.full_sentence

	def make_part_a(self):
		if "!(" in self.full_sentence and not self.halves:
			self.halves = self.full_sentence.split("!")
		if self.halves:
			return self.halves[0]

	def make_part_b(self):
		if "!(" in self.full_sentence and not self.halves:
			self.halves = self.full_sentence.split("!")
		if self.halves:
			return self.halves[1]


class QuestionConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		if wrapped.sentence.get_q_word() in ["do", "does", "can"]:
			self.full_sentence =  f"4. {wrapped.sentence.get_q_word()} {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {wrapped.sentence.get_num_nouns()} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}? "
		elif wrapped.sentence.get_q_word() == "there":
			self.full_sentence =  f"5. {wrapped.sentence.get_verb()} {wrapped.sentence.get_q_word()} {wrapped.sentence.get_num_nouns()} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} ?"

class StatementConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		if wrapped.sentence.get_q_word() == "there":
			# There are ..
			counter = p.number_to_words(wrapped.sentence.get_num_nouns())
			if counter == "zero":
				counter = wrapped.sentence.get_num_nouns()
			self.full_sentence = f"3. {wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {counter} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."
		else:
			#Something's a bit wonky with the logic...
			#Maybe there's a better way to combine counter + adj + noun with inflect
			if wrapped.ignore_do:
				# He eats 5 potatoes
				self.full_sentence = f"1. {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "
			elif wrapped.sentence.get_q_word():
				# He can eat 5 potatoes
				self.full_sentence = f"2a. {wrapped.sentence.get_subj()} {wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "
			else:
				# He eats 5 potatoes
				self.full_sentence = f"2b. {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "


def sort_modified_s_obj(sentence_object):
	if sentence_object.is_question:
		return QuestionConstruction(sentence_object.get_wrapped_sentence_obj())#.make_full_sentence()

	else:
		return StatementConstruction(sentence_object.get_wrapped_sentence_obj())#.make_full_sentence()




s_obj = sentence_object.get_s_obj()
mo_obj = sentence_grammar.FIBV_sentence_obj(s_obj)
print(sort_modified_s_obj(mo_obj))
mo_obj2 = sentence_grammar.FIBN_sentence_obj(s_obj)
print(sort_modified_s_obj(mo_obj2))
mo_obj3 = sentence_grammar.FS_sentence_obj(s_obj)
print(sort_modified_s_obj(mo_obj3))
mo_obj4 = sentence_grammar.Question_sentence_obj(s_obj)
print(sort_modified_s_obj(mo_obj4))