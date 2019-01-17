import sentence_template as sentence_template


# def generate_FIB_verb(sentence_object):
# 	return sentence_template.FillInTheBlanks_Verb(sentence_object).set_plural_nouns().set_blank().get_sentence()

# def generate_FIB_noun(sentence_object):
# 	return sentence_template.FillInTheBlanks_Noun(sentence_object).set_plural_verbs().set_blank().get_sentence()

# def generate_FIB_YNQ(sentence_object):
# 	return sentence_template.FillInTheBlanks_YesNoQ(sentence_object).set_plural_nouns().set_blank().get_sentence()

def modified_sentence_object(sentence_object):
	return sentence_template.SentenceTemplate(sentence_object).set_question().set_plural_verbs().get_wrapped_sentence_obj()


