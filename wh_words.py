# Generates question words for the sentence objects
#
# Stephanie Leung (2019)
from random import choice

def get_question_word():
	return choice(["can", "does", "there", False, False])



# Notes:
# - Implement open ended wh-words
# - Once that happens probably should switch to file reading instead of listing it in the codes