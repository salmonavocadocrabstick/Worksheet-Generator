# Sentence Object Builder Unit Test
#
# Stephanie Leung (2019)
from sentence_obj_builder import SentenceObject
import unittest

class SentenceObjectTests(unittest.TestCase):
	def setUp(self):
		self.sobj = SentenceObject("I", "eat", "funny", "potatoes", "")

	def test_init(self):
		self.assertEqual(self.sobj.subj, "I")
		self.assertEqual(self.sobj.num_subj, 0)
		self.assertEqual(self.sobj.v_type, None)
		self.assertEqual(self.sobj.verb, "eat")
		self.assertEqual(self.sobj.adj, "funny")
		self.assertEqual(self.sobj.num_nouns, 0)
		self.assertEqual(self.sobj.noun, "potatoes")
		self.assertEqual(self.sobj.q_word, "")
		self.assertEqual(self.sobj.is_q, False)
		self.assertEqual(self.sobj.tense, "present")

	def test_get_set_functs(self):
		self.sobj.set_noun("strawberries")
		self.sobj.set_verb("cut")
		self.sobj.set_num_nouns(3)
		self.sobj.set_num_subj(2)
		self.sobj.set_q_word("Do")
		self.sobj.set_is_q(True)

		self.assertEqual(self.sobj.get_noun(),"strawberries")
		self.assertEqual(self.sobj.get_verb(),"cut")
		self.assertEqual(self.sobj.get_num_nouns(), 3)
		self.assertEqual(self.sobj.get_num_subj(), 2)
		self.assertEqual(self.sobj.get_q_word(), "Do")
		self.assertEqual(self.sobj.get_is_q(), True)
		#self.assertEqual(self.sobj.get_subj(), "I")

if __name__ == "__main__":
	unittest.main()

