# Sentence Object Builder Unit Test
#
# Stephanie Leung (2019)

from sentence_obj_builder import SentenceObject, SentenceObjectBuilder
import unittest

class SentenceObjectBuilderTests(unittest.TestCase):
	def setUp(self):
		print(">> Setting up Sentence Builder Object.....\n")
		self.genSObj = SentenceObjectBuilder().gen_subj().gen_verb().gen_noun().gen_quantity().gen_adjective().gen_question_word().get_sentence_object()

	def test_init(self):
		print("Testing sentence object initialization....\n")
		self.assertTrue(isinstance(self.genSObj, type(SentenceObject())))

	def test_deepcopy(self):
		'''The noun stored in sentence object is not the same as the noun that is given to
		the sentence constructor. Since directly changing the noun would have unwanted effects,
		each time the noun, verb is returned, it is actually the deep copied version of it, not the reference of the original obj.'''
		print("Testing sentence object deep copy....\n")
		t_noun = self.genSObj.get_noun()
		t_verb = self.genSObj.get_verb()

		self.genSObj.noun = "_changing_into_crazy_noun_"
		self.genSObj.verb = "_changing_into_crazy_verb_"

		print(f"Expecting {t_noun} is not the same as {self.genSObj.noun}")
		self.assertNotEqual(t_noun, id(self.genSObj.noun))
		print(f"Expecting {t_verb} is not the same as {self.genSObj.verb}")
		self.assertNotEqual(t_verb, id(self.genSObj.verb))

	def test_gen_without_v_type(self):
		'''Noun, adjective generation are dependent of verb type. 
		This test checks that noun and adjectives will not be generated when verb type is missing.'''
		print("Testing raise Exceptions............\n")
		self.assertRaises(Exception, SentenceObjectBuilder().gen_noun)
		self.assertRaises(Exception, SentenceObjectBuilder().gen_adjective)
		self.assertRaises(Exception, SentenceObjectBuilder().gen_quantity)
		self.assertRaises(Exception, SentenceObjectBuilder().gen_adjective)

	def test_gen_with_v_type(self):
		print("Testing generation functions............\n")
		try:
			SentenceObjectBuilder().gen_verb().gen_noun()
		except Exception:
			self.fail("Gen_Noun raised Exception unexpectedly.")

		try:
			SentenceObjectBuilder().gen_verb().gen_adjective()
		except Exception:
			self.fail("gen_adjective raised Exception unexpectedly.")

		try:
			SentenceObjectBuilder().gen_verb().gen_quantity()
		except Exception:
			self.fail("gen_adjective raised Exception unexpectedly.")

if __name__ == "__main__":
	unittest.main()

