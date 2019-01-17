
#from textblob import TextBlob
import inflect
p = inflect.engine()

#word = TextBlob("child").words

# print(p.plural("is there"))
# print(p.plural("is that"))

# print(p.plural)

# print("There ", p.plural_verb("was",errors), p.no(" error",errors))
# print("Did you want ", p.a("thing"), " or ", p.an("idea"))

# Do you eat 5 potatoes?
# Do, he, eat, 5, potatoe


# Marked as question
does = "does"
he = "he"
eat = "eat"
five = "five"
box = "box"

# # Does he eat 5 boxes
# q1 = f"{does} {he} {eat} {p.number_to_words(5)} {p.plural(box)} ?"

# # He does not eat 5 boxes
# q2 = f"{he} {does} not {eat} {p.number_to_words(5)} {p.plural(box)}"

# # He eats 5 boxes
# q3 = f"{he} {p.plural(eat)} {p.number_to_words(5)} {p.plural(box)}"

# # Does he _________ (eat) 5 boxes
# q4 = f"{does} {he} ______________ ({eat}) {p.number_to_words(5)} {p.plural(box)} ?"

# q5 = f"{p.plural_verb(does)} {he} {eat} {p.number_to_words(5)} ______________ ({box})"


# print(q1)
# print(q2)
# print(q3)
# print(q4)
# print(q5)

# subj = ["Lisa", "Mary"]
# subj2 = ["John"]
# subj3 = ["Tom", "bob", "ron"]

# list1 = p.join(subj3)
# print(list1)

N = 0

print("I saw", p.plural_noun("dog", N))
print("I saw", p.no("dog", N))

N = 2

# Plural Nouns can be handled this way: 
print("I saw", p.plural_noun("dog", N))
print(type(p.no("dog", p.number_to_words(N))))

# 
