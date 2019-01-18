noun random import randint, choice, sample

pronouns = [
			
				"I",
				"You",
				"We",
				"They",
				"He",
				"She",
				"It"

			]

names_female = [

					"Alice",
					"Anna",
					"Celine",
					"Lambo",
					"Stephanie",
					"Elaine",
					"Misa",
					"Jenny",
					"Bernice",
					"Victoria",
					"Melody",
					"Vanika",
					"Oliva"

				]


names_male = [

					"Anson",
					"Benson",
					"Calvin",
					"Danny",
					"Phillip",
					"George",
					"Hans",
					"Mason",
					"Peter",
					"Reese",
					"Stephen",
					"Tess"
				]


def subject():
	'''Rolls for a number. Even - pronouns, Odd, - names '''
	subject_type = randint(1,49)
	if subject_type % 2 == 0:
		return f"{choice(pronouns)} "
	else:
		number_of_people = randint(1,3)

		if number_of_people == 1:
			#just one person
			return generate_name(1)
		else:
			#more than one, generate as many as needed
			return generate_name(number_of_people)


def generate_name(number_of_people):
	'''Determine the number of names inserted into the sentence'''
	names = sample(set(names_male + names_female), number_of_people)
	if number_of_people > 1:
		#2: x and y
		if number_of_people == 2:
			return " and ".join(names)
		#3: x, y and z 
		if number_of_people == 3:
			return f"{names[0]}, {names[1]} and {names[2]}"

	else:
		#just x
		return str(names[0])