import sentence_template as sentence_template

def generate_FIB_verb(sentence_object):
	return sentence_template.FillInTheBlanks_Verb(sentence_object).set_plural_nouns().set_blank().get_sentence()

def generate_FIB_noun(sentence_object):
	return sentence_template.FillInTheBlanks_Noun(sentence_object).set_plural_verbs().set_blank().get_sentence()




