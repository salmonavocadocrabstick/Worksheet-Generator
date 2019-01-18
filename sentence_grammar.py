import sentence_template as sentence_template


# def generate_FIB_verb(sentence_object):
# 	return sentence_template.FillInTheBlanks_Verb(sentence_object).set_plural_nouns().set_blank().get_sentence()

# def generate_FIB_noun(sentence_object):
# 	return sentence_template.FillInTheBlanks_Noun(sentence_object).set_plural_verbs().set_blank().get_sentence()

# def generate_FIB_YNQ(sentence_object):
# 	return sentence_template.FillInTheBlanks_YesNoQ(sentence_object).set_plural_nouns().set_blank().get_sentence()

def FIBV_sentence_obj(sentence_object):
	return sentence_template.FillInTheBlanks_Verb(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def FIBN_sentence_obj(sentence_object):
	return sentence_template.FillInTheBlanks_Noun(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def FS_sentence_obj(sentence_object):
	return sentence_template.FullSentence(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def Q_sentence_obj(sentence_object):
	return sentence_template.FullSentence(sentence_object).process_s_obj(set_question=True).get_wrapped_sentence_obj()