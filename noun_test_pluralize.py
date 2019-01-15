
#from textblob import TextBlob
import inflect
infl = inflect.engine()

#word = TextBlob("child").words

print(infl.plural("kiss"))
print(infl.plural("tomato"))

print(infl.plural)