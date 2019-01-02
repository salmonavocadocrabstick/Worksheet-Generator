from bs4 import BeautifulSoup
import requests
import re

def get_noun_list():
	timestamp = "time_record.txt"
	noun_bank = "noun_bank.txt"

	today = date.today()
	need_to_scrape = False


	try:
		with open(timestamp, "r+") as time_file:
			last_time = time_file.read()
			last_time = last_time.split("-")
			#print(last_time)
			if date(today.year, today.month, 28) > date(int(last_time[0]), int(last_time[1]), 28):
				time_file.seek(0)
				time_file.write(str(today))
				#need_to_scrape = True
				scrape_noun_list()
	except FileNotFoundError:
		scrape_noun_list()
	finally:
		pass


	with open(noun_bank, "r") as nouns:
		noun_list = nouns.read().split(" ")[:-2:]

	return noun_list

def scrape_noun_list(noun_url, noun_bank):

	res = requests.get(noun_url)


	soup = BeautifulSoup(res.text, "html.parser")
			# nouns = soup.find(class_="item-page").select("p")[firstword].get_text()

	#CHANGE HERE TO FIND THE RIGHT ITEM
	records = soup.find_all(class_="wordlist-item")
	#print(records)

	#Change or block out
	#pattern = re.compile(r"^[0-9]{1,3}\.\s(\b[a-z]*\b$)")

	with open(noun_bank, "w") as noun_file:
		for word in range(2, len(records)-1):
			#match = pattern.search(records[word].get_text())
			#if match:
				#regex_word = pattern.sub("\g<1>", records[word].get_text())
				regex_word = records[word].get_text()
				noun_file.write(regex_word + "\n")


noun_url = "https://www.enchantedlearning.com/wordlist/fruit.shtml"
new_file_name = "noun_food.txt"
scrape_noun_list(noun_url, new_file_name)



# Scraped:
# Nouns: https://stickyball.net/esl-grammar-worksheets.html?id=85
# Appliances : https://www.enchantedlearning.com/wordlist/householddevices.shtml
# Fruit: https://www.enchantedlearning.com/wordlist/fruit.shtml