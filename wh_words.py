# # Generates question words for the sentence objects
# #
# # Stephanie Leung (2019)

from numpy.random import choice

def get_question_word():
	q_word_choices = ["does","there", "can"]
	return choice(q_word_choices,  p=[0.6, 0.3, 0.1])
	#return choice(["this", "that"])


# Notes:
# - Implement open ended wh-words
# - Once that happens probably should switch to file reading instead of listing it in the codes
# - 1/19/2019 - Implementing numpy.random.choice for weighted random.

