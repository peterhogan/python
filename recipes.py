class Book(object):

	# The main book, from which you can add recipes, 

	def __init__(self, name):
		self.name = name


	def add(self):
		title = raw_input("What is the recipe for? ")
		print """Which meal is the recipe for?
	1). Breakfast
	2). Lunch
	3). Tea
	4). Any/None/Snack"""
		meal_choose = input("Please choose 1, 2, 3 or 4: ")
		if meal_choose is 3:
			print """Which course is the recipe for?
	1). Starter
	2). Main
	3). Dessert
	4). Aperitif
	5). Other"""
			course_choice = input("Please choose between 1 and 5: ")

class MainMenu(object):
	print "Pick a recipe book please:"
	
	print """What would you like to do? (Please just enter a number):
	1). Read a recipe 
	2). Browse recipes
	3). Cook a meal
	4). Add/edit a recipe
	
	menu_choice1 = input("? ") 


class LoadSave:
	


class Recipe(object):
	
	# recipes have titles, ingredients (which have amounts), 
	# steps, time taken, classifications(starter, main, dessert), 
	# difficulty, number served and time of day (morning, lunch, evening, other).

	def __init__(self, title, ingredients, steps, time, course, difficult, serves, meal):
		self.title = title
		self.ingedients = ingredients
		self.steps = steps
		self.time = time
		self.course = course
		self.difficult = difficult
		self.serves = serves
		self.meal = meal


	def read(self):
		print """What would you like to see?:
		1). Ingredients needed
		2). Time taken
		3). Difficulty
		4). People served
		5). All of the recipe"""
		choice = input("...? ")

	def edit(self):
		pass
		

book = Book("My Recipes")

book.add()

fajitas = Recipe("Fajitas", ["chicken","peppers","garlic"], 4, 20, "Main", "Easy", 4, "Evening")

fajitas.read()
