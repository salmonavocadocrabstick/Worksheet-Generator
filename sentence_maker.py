

# This class constructs the sentences with the given words
# Does not add any grammar rules
# Checks what words are available 
# and generates sentences according to the words

# Again, it DOES NOT ADD ANY GRAMMAR RULES YOU CRAZY OLD BAT

import sentence_element_builder as sentence_object
import sentence_grammar as sentence_grammar
import inflect
p = inflect.engine()


# class SentenceConstruction:

# 	def make_full_sentence(self, sentence):
# 		#return f"{sentence.subj.subjects[0]} {sentence.verb[1]} {sentence.num_nouns} {sentence.adj} {sentence.noun[0]}."
# 		pass

# 	def make_first_half(self):
# 		# construct first half here
# 		pass

# 	def make_second_half(self):
# 		# cosntruct second half here
# 		pass

# 	def make_question(self):
# 		if sentence.get_q_word()[0] is True and sentence.get_word()[1]:
# 			pass


class SentenceConstruction():
	def make_full_sentence(self):
		if self.full_sentence:
			return self.full_sentence


class FIB_SentenceConstruction(SentenceConstruction):
	def __init__(self, FIB):
		self.full_sentence = f"{FIB.subj.subjects[0]} {FIB.verb[1]} {FIB.num_nouns} {FIB.adj} {FIB.noun}"
		self.halves = self.sentence.split('!')

	def make_first_half(self):
		return self.halves[0]
	def make_second_half(self):
		return self.halves[1]


class QuestionConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		if wrapped.sentence.get_q_word() in ["do", "does", "can"]:
			self.full_sentence =  f"4. {wrapped.sentence.get_q_word()} {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {wrapped.sentence.num_nouns} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}? "
		elif wrapped.sentence.get_q_word() == "there":
			self.full_sentence =  f"5. {wrapped.sentence.get_verb()} {wrapped.sentence.get_q_word()} any {wrapped.sentence.adj} {wrapped.sentence.get_noun()} ?"

class StatementConstruction(SentenceConstruction):
	def __init__(self, wrapped):
		if wrapped.sentence.get_q_word() == "there":
			number_words = {p.number_to_words(wrapped.sentence.get_num_nouns())}
			if wrapped.is_neg:
				number_words = "any"
			self.full_sentence = f"3. {wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {number_words} {wrapped.sentence.adj} {wrapped.sentence.get_noun()}."
		else:
			#Something's a bit wonky with the logic...
			#Maybe there's a better way to combine counter + adj + noun with inflect
			if wrapped.ignore_do:
				self.full_sentence = f"1. {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "
			elif wrapped.sentence.get_q_word():
				self.full_sentence = f"2a. {wrapped.sentence.get_subj()} {wrapped.sentence.get_q_word()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "
			else:
				self.full_sentence = f"2b. {wrapped.sentence.get_subj()} {wrapped.sentence.get_verb()} {p.number_to_words(wrapped.sentence.get_num_nouns())} {wrapped.sentence.adj} {wrapped.sentence.get_noun()} "
# class NegativeStatement(SentenceConstruction):
# 	def __init__(self, sentence):


def sort_modified_s_obj(sentence_object):
	if sentence_object.is_question:
		return QuestionConstruction(sentence_object.get_wrapped_sentence_obj()).make_full_sentence()

	else:
		return StatementConstruction(sentence_object.get_wrapped_sentence_obj()).make_full_sentence()




s_obj = sentence_object.get_s_obj()
print(s_obj.get_subj())
print(s_obj.get_subj())
print(s_obj.get_subj())
print(s_obj.get_subj())
print(type(s_obj))
print( f">>> {s_obj.get_verb()} {s_obj.get_q_word()} any {s_obj.adj} {s_obj.get_noun()} " )
mo_obj = sentence_grammar.modified_sentence_object(s_obj)
print(sort_modified_s_obj(mo_obj))
