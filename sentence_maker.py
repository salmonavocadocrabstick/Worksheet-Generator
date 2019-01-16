

# This class constructs the sentences with the given words
# Does not add any grammar rules
# Checks what words are available 
# and generates sentences according to the words

# Again, it DOES NOT ADD ANY GRAMMAR RULES YOU CRAZY OLD BAT



class SentenceConstruction:
	def make_full_sentence(self, sentence):
		return f"{sentence.subj.subjects[0]} {sentence.verb[1]} {sentence.num_nouns} {sentence.adj} {sentence.noun[0]}."

	def make_first_half(self):
		# construct first half here
		pass

	def make_second_half(self):
		# cosntruct second half here
		pass

	def make_question(self):
		pass


class FIB_SentenceConstruction(SentenceConstruction):
	def __init__(self, FIB):
		self.sentence = f"{FIB.subj.subjects[0]} {FIB.verb[1]} {FIB.num_nouns} {FIB.adj} {FIB.noun}"
		self.halves = self.sentence.split('!')
		print(self.halves)

	def make_first_half(self):
		return self.halves[0]
	def make_second_half(self):
		return self.halves[1]

class Q_SentenceConstruction(SentenceConstruction):
	pass
