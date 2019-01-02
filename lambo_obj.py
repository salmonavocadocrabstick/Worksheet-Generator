from random import choice, randint
from bs4 import BeautifulSoup
import requests
import re

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
	<p style="text-align: center;"><span style="font-size: 14pt;">1. word</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">2. letter</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">3. number</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">4. person</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">5. pen</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">6. class</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">7. people</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">8. sound</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">9. water</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">10. side</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">11. place</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">12. man</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">13. men</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">14. woman</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">15. women</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">16. boy</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">17. girl</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">18. year</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">19. day</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">20. week</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">21. month</span><span id="ezoic-pub-ad-placeholder-114" class="ezoic-adpicker-ad"></span><span style="float: none; min-height: 270px; min-width: 250px; display: block; margin: 2px 0px !important; text-align: center !important;" class="ezoic-ad medrectangle-3 adtester-container adtester-container-114" data-ez-name="stickyball_net-medrectangle-3"><span id="div-gpt-ad-stickyball_net-medrectangle-3-0" ezaw="250" ezah="250" style="position: relative; z-index: 0; display: inline-block; min-height: 250px; min-width: 250px;" class="ezoic-ad"><script data-cfasync="false" type="text/javascript" style="display:none;">eval(ez_write_tag([[250,250],'stickyball_net-medrectangle-3','ezslot_2']));</script><div id="google_ads_iframe_/1254144/stickyball_net-medrectangle-3_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1254144/stickyball_net-medrectangle-3_0" title="3rd party ad content" name="google_ads_iframe_/1254144/stickyball_net-medrectangle-3_0" width="250" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" style="border: 0px; vertical-align: bottom;"></iframe></div></span></span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">22. name</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">23. sentence</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">24. line</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">25. air</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">26. land</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">27. home</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">28. hand</span></p>
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
	<p style="text-align: center;"><span style="font-size: 14pt;">42. school</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">43. plant</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">44. food</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">45. sun</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">46. state</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">47. eye</span><span id="ezoic-pub-ad-placeholder-115" class="ezoic-adpicker-ad"></span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">48. city</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">49. tree</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">50. farm</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">51. story</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">52. sea</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">53. night</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">54. day</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">55. life</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">56. north</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">57. south</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">58. east</span><span id="ezoic-pub-ad-placeholder-116" class="ezoic-adpicker-ad"></span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">59. west</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">60. child</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">61. children</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">62. example</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">63. paper</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">64. music</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">65. river</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">66. car</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">67. foot</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">68. feet</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">69. book</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">70. science</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">71. room</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">72. friend</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">73. idea</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">74. fish</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">75. mountain</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">76. horse</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">77. watch</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">78. color</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">79. face</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">80. wood</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">81. list</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">82. bird</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">83. body</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">84. dog</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">85. family</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">86. song</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">87. door</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">88. product</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">89. wind</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">90. ship</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">91. area</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">92. rock</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">93. order</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">94. fire</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">95. problem</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">96. piece</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">97. top</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">98. bottom</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">99. king</span></p>
	<p style="text-align: center;"><span style="font-size: 14pt;">100. space</span></p>
	<p>&nbsp;</p>
	
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


#noun_url = "https://stickyball.net/esl-grammar-worksheets.html?id=85"
#es = requests.get(noun_url)
soup = BeautifulSoup(pract_str, "html.parser")
# print(soup.get_text())
# nouns = soup.find(class_="item-page").select("p")[2]
#print(nouns.get_text(strip=True))
#word = 2
# nouns = soup.find(class_="item-page").select("p")[firstword].get_text()
records = soup.find(class_="item-page").select("p")
words_only = []
for word in range(2, len(records)-1):
	words_only.append(records[word].get_text())

print(words_only)
