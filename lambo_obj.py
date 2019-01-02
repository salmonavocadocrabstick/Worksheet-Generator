from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re
from time import time

nouns = 	[
				"jacket",
				"jumper",
				"sneaker",
				"sunglasses",
				"skirt",
				"bracelet",
				"ring",
				"egg",
				"juice"
			]


adjectives = [
				"warm",
				"cozy",
				"comfortable",
				"lovely",
				"beautiful",
				"sparkly",
				"fun-looking",
				"white",
				"blue",
				"red"
			]


pract_str = """
<div class="clearpad">
<div class="item-page">
	<h1 style="text-align: center;"><span style="color: #b22222;">ESL Grammar</span><span id="ezoic-pub-ad-placeholder-107" class="ezoic-adpicker-ad"></span><span style="float: none; min-height: 110px; min-width: 728px; display: block; margin: 2px 0px !important; text-align: center !important;" class="ezoic-ad box-3 adtester-container adtester-container-107" data-ez-name="stickyball_net-box-3"><span id="div-gpt-ad-stickyball_net-box-3-0" ezaw="728" ezah="90" style="position: relative; z-index: 0; display: inline-block; min-height: 90px; min-width: 728px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[728,90],'stickyball_net-box-3','ezslot_1']));</script><div id="google_ads_iframe_/1254144/stickyball_net-box-3_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144/stickyball_net-box-3_0" title="3rd party ad content" name="google_ads_iframe_/1254144/stickyball_net-box-3_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" style="border: 0px; vertical-align: bottom;"></iframe></div></span></span></h1>
	<h2 style="text-align: center;"><span style="font-size: 14pt;"><strong>List of 100 Common Nouns</strong></span></h2>
	<p style="text-align: center;">This page lists 100 of the most common nouns in the English language.</p>
	<p>&nbsp;</p>
	<p style="text-align: center;"><span style="font-size: 14pt;">29. house</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">30. picture</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">31. animal</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">32. mother</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">33. father</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">34. brother</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">35. sister</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">36. world</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">37. head</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">38. page</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">39. country</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">40. question</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">41. answer</span></p>

	
<span id="ezoic-pub-ad-placeholder-118" class="ezoic-adpicker-ad"></span><span style="float: none; min-height: 270px; min-width: 300px; display: block; margin: 2px 0px !important; text-align: center !important;" class="ezoic-ad medrectangle-1 adtester-container adtester-container-118" data-ez-name="stickyball_net-medrectangle-1"><span id="div-gpt-ad-stickyball_net-medrectangle-1-0" ezaw="300" ezah="250" style="position: relative; z-index: 0; display: inline-block; min-height: 250px; min-width: 300px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[300,250],'stickyball_net-medrectangle-1','ezslot_3']));</script><div id="google_ads_iframe_/1254144/stickyball_net-medrectangle-1_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144/stickyball_net-medrectangle-1_0" title="3rd party ad content" name="google_ads_iframe_/1254144/stickyball_net-medrectangle-1_0" width="300" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" style="border: 0px; vertical-align: bottom;"></iframe></div></span><span style="width:300px;display:block;height:14px;margin:auto" class="reportline"><span style="text-align:center;font-size: smaller;float:left;line-height:normal;"><a href="https://www.ezoic.com/what-is-ezoic/" target="_blank" style="cursor:pointer"><img src="https://go.ezoic.net/utilcave_com/img/ezoic.png" style="height:12px !important; padding:2px !important; border:0px !important; cursor:pointer !important; width: 58px !important; margin:0 !important; box-sizing: content-box !important;"></a></span><span id="ez-report-ad-button" name="?pageview_id=644d8a5c-9ec4-4388-6b86-f338fe7a6394&amp;ad_position_id=118&amp;impression_group_id=stickyball_net-medrectangle-1/2019-01-02/211667&amp;ad_size=300x250&amp;domain_id=707&amp;url=https://stickyball.net/esl-grammar-worksheets.html?id=85" style="cursor: pointer!important; font-size:12px !important;color: #a5a5a5 ;float:right;text-decoration:none !important;font-family:arial !important;line-height:normal;">report this ad</span></span></span></div>
 </div>"""


def object():
	decision = randint(1, 5)
	if decision < 2:
		return f"a {noun_or_adj_noun()}"
	else:
		return f"{decision} {noun_or_adj_noun()}s"


def noun_or_adj_noun():
	decision = randint(1, 100)
	if decision % 2 == 0:
		return noun_only()		#noun only
	else:
		return adj_noun()		#return adj_noun

def noun_only():
	return f"{choice(nouns)}"

def adj_noun():
	return f"{choice(adjectives)} {choice(nouns)}"


try:
	with open("time_record.txt", "r") as time_file:
		last_time = time_file.read()
except FileNotFoundError:
	pass



#noun_url = "https://stickyball.net/esl-grammar-worksheets.html?id=85"
#es = requests.get(noun_url)
soup = BeautifulSoup(pract_str, "html.parser")
# nouns = soup.find(class_="item-page").select("p")[firstword].get_text()
records = soup.find(class_="item-page").select("p")
text_only = []
pattern = re.compile(r"^[0-9]{1,3}\.\s(\b[a-z]*\b$)")

for word in range(2, len(records)-1):
	match = pattern.search(records[word].get_text())
	if match:
		regex_word = pattern.sub("\g<1>", records[word].get_text())
		text_only.append(regex_word)


#print(text_only)

# for word in text_only:
	# match = pattern.search(word)
	# if match:
	# 	print("True")
	# else:
	# 	print("False")



