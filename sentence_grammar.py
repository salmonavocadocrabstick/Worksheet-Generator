import sentence_template as sentence_template



def FIBV_sentence_obj(sentence_object):
	return sentence_template.FillInTheBlanks_Verb(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def FIBN_sentence_obj(sentence_object):
	return sentence_template.FillInTheBlanks_Noun(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def FS_sentence_obj(sentence_object):
	return sentence_template.FullSentence(sentence_object).process_s_obj().get_wrapped_sentence_obj()

def Q_sentence_obj(sentence_object):
	return sentence_template.FullSentence(sentence_object).process_s_obj(set_question=True).get_wrapped_sentence_obj()


#def sort_modified_s_obj(sentence_object):
#	if sentence_object.is_question:
#		sentence_template.QuestionConstruction(sentence_object.get_wrapped_sentence_obj()).make_full_sentence()

#	else:
#		sentence_template.StatementConstruction(sentence_object.get_wrapped_sentence_obj()).make_full_sentence()

