
from textblob import TextBlob

word = TextBlob("child").words

print(type(word.pluralize()))