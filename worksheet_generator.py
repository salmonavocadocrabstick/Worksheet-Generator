# import objects_gen as obj
# import verbs_gen as vrb
# import subjects_gen as subj
# import pres_keywords_gen as pre
#import sentence_template as sentence_template
import sentence_element_builder as sentence_object
import sentence_grammar as sentence_grammar
import sentence_maker as s_make

from docx import Document
from docx.shared import Pt #for font size
from docx.enum.style import WD_STYLE_TYPE
from datetime import date


def _FIB(FIB_obj):
	FIB_sentence = s_make.generate_sentence_by_type(FIB_obj)
	print(FIB_sentence.get_full_sentence())
	#Careful: x is accessed without explicit definition here...
	p = document.add_paragraph(f"{x}. {FIB_sentence.get_part_a()}", style = "Normal")
	p.add_run("______________").font.name = "Comic Sans"
	p.add_run(f"{FIB_sentence.get_part_b()}")

def Fill_In_The_Blanks_Verbs(s_obj):
	FIBV_obj = sentence_grammar.FIBV_sentence_obj(s_obj)
	_FIB(FIBV_obj)

def Fill_In_The_Blanks_Nouns(s_obj):
	FIBV_obj = sentence_grammar.FIBN_sentence_obj(s_obj)
	_FIB(FIBV_obj)

def Answering_Questions(s_obj):
	AQ_obj = sentence_grammar.Q_sentence_obj(s_obj)
	AQ_sentence = s_make.generate_sentence_by_type(AQ_obj)
	print(AQ_sentence.get_full_sentence())

	## Getting a list of shuffled words, just pop them one by one in the for loop!.

	document.add_paragraph(f"{x}. {AQ_sentence.get_full_sentence()}", style = "Normal")
	document.add_paragraph("________________________________________________")

def Finding_Mistakes(s_obj):
	FM_obj = sentence_grammar.Q_sentence_obj(s_obj)
	FM_sentence = s_make.generate_sentence_by_type(FM_objects)
	print(AQ_sentence.get_full_sentence())
	document.add_paragraph(f"{x}. {AQ_sentence.get_full_sentence()}", style = "Normal")

def Rearrage_Sentences(s_obj):
	pass


if __name__ == "__main__":
	#Variables
	doc_title = "Verbs"
	instruction = [
						"Fill in the blanks with the correct verb.", #0
						"Fill in the blanks with the correct noun.",
						"Rearrange the sentences into the correct order.",
						"Answer the following questions in full sentences."

					]
	doc_instru = instruction[0]


	num_questions = 50


	document = Document()


	styles = document.styles

	# Title:
	heading_style = styles.add_style('Heading St', WD_STYLE_TYPE.PARAGRAPH)
	heading_style.base_style = styles["Heading 1"]
	heading_style.font.name = "Janda Manatee Bubble"
	heading_style.font.size = Pt(30)

	document.add_paragraph(doc_title, style = "Heading St")

	#Document Styling
	style = document.styles["Normal"]
	font = style.font
	font.name = "Architect"
	font.size = Pt(18)

	document.add_heading(doc_instru, level=2)


	for x in range(1, num_questions+1):
		s_obj = sentence_object.get_s_obj()

		### Run the function here ###
		Answering_Questions(s_obj)
		

	document.add_page_break()
	document.save(f"{doc_title}_{date.today()}.docx")

	print(f"Worksheet {doc_title}_{date.today()}.docx is generated in designated folder.")