import objects_gen as obj
import verbs_gen as vrb
import subjects_gen as subj
import pres_keywords_gen as pre
#import sentence_template as sentence_template
import sentence_element_builder as sentence_object
import sentence_grammar as sentence_grammar
import sentence_maker as s_make

from docx import Document
from docx.shared import Pt #for font size
from datetime import date


#Variables
doc_title = "Verbs"
instruction = [
					"Fill in the blanks with the correct verb.", #0
					"Fill in the blanks with the correct noun."
					"Rearrange the sentences into the correct order."

				]
doc_instru = instruction[0]
num_questions = 10


document = Document()
document.add_heading(doc_title, 0)

#Document Styling
style = document.styles["Normal"]
font = style.font
font.name = "KG Neatly Printed Spaced"
font.size = Pt(18)



document.add_heading(doc_instru, level=1)


for x in range(1, num_questions+1):
	# verb_list = vrb.verb()
	# verb = verb_list[1]
	# #print(verb)
	# adj_noun = obj.object(verb_list[0], 1) #stop s being added to nouns
	# #print(adj_noun)
	
	# subject = subj.subject()
	# keyword = pre.present_tense_keyword()

	#Fill in the blanks
	#s_obj = sentence_object.SentenceObjectBuilder().set_subj().set_verb().set_noun().set_quantity().set_adjective().get_sentence_obj()
	s_obj = sentence_object.get_s_obj()
	FIBV = sentence_grammar.generate_FIB_verb(s_obj)
	p = document.add_paragraph(f"{x}. {s_make.FIB_SentenceConstruction(FIBV).make_first_half()}", style = "Normal")
	p.add_run("______________").font.name = "Comic Sans"
	p.add_run(f"{s_make.FIB_SentenceConstruction(FIBV).make_second_half()}.")

document.add_page_break()
document.save(f"{doc_title}_{date.today()}.docx")

print(f"Worksheet {doc_title}_{date.today()}.docx is generated in designated folder.")