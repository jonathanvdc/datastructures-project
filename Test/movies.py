import randomrng = random.Random()
# Collection of nouns that describe concepts
movieTitleConcepts = [ "Life", "Death", "Power", "Strength", "Wisdom", "Defiance", "Truth",
							"Lies", "Acceptance", "Forgiveness", "Murder", 
							"Joy", "Sorrow", "Fury", "Fear", "Pain", "War", "Honor", "Duty", "Guardian"]

# Collection of nouns that describe objects
movieTitleObjects = 	[ "Dawn", "Burn", "Story", "Legacy", "Birth", "Galaxy", "Guardian",
							"Interview",  "Grit", "Cop", "Shark", "Room", "Fight", "Knife", "America",
							"Shank", "Thing", "Snake", "Gun", "Gear", "Tendency", "Sword", "Russia",
							"Blade", "Godfather", "Odyssey", "Walker", "Boyhood", "Activity",
							"Massacre", "Chainsaw", "Eater", "Fist", "Werewolf", "Vampire", "Boss"]
# Collection of nounsmovieTitleNouns = movieTitleConcepts + movieTitleObjects
# Collection of adjectivesmovieTitleAdnouns = [ "Hot", "Cold", "Light", "Gone", "Big",  "Dark", "Pacific", "Bold", 							"Horrible", "True", "Solid", "Golden", "Red", "Scary", "Paranormal",
							"Black", "Unbreakable", "American", "Russian", "Righteous", "Heroic",
							"Dangerous", "Lethal", "Global", "Viral", "Real"]# Collection of nouns that double as adjectives, and adjectives that double as nounsmovieTitleDoubles = [ "Alien", "Liberty", "Hobbit", "Monster", "Robot", "American", "Russian",							"Cyborg", "Ninja", "Machine", "Predator", "Stone", "Steel", "Space", 							"Diamond", "Metal", "Fear", "Death", "Blood", "Heat", "Fallen", 							"Peace", "Ghost", "Phantom", "Battle", "Enemy", "Hostile", "Expendable",
							"Mutant", "Nightmare", "Texas"]
							

							
# Collection of starts to a movie subtitlemovieSubtitleStarts = ["Revenge of", "Attack of", "Return of",							"Story of", "A Tale of", "Requiem for", "A New",							"End of the", "Eternal Sunshine of", "Call for", "Call of",							"Death of the", "Passion of", "Memories of", "The Phantom",							"Sons of the", "Guns of the", "Prepare for", "The Missing", "Lost",							"A Dystopian", "Unlimited", "Grandpa's", "A Space", "The Dark",							"The Smell of", "The Final", "Enter the", "The Usual", "The Big"]

# Collection of ends to a movie subtitlemovieSubtitleEnds = ["Strikes Back", "Harder", "Menace", "Awakens", 							"Annihilation", "of Power", "of Fury", "With a Cause",							"Again", "Better", "Faster", "Stronger", "Justice",							"Wizard", "Redemption", "Vengeance", "of Liberty",							"from Space", "from Beneath", "from Hell", "After Dark"]						def chance_out_of(x, y):
	""" Has X chance out of Y to return True. """	return rng.randint(1, y) <= x						def flip_coin():
	""" Has 1 chance out of 2 to return True. """	return chance_out_of(1, 2)def random_elem(list):
	""" Returns a random element from a given list. """	return list[rng.randrange(0, len(list))]
	
def make_multiple(string):
	""" Takes a string ending in a noun and changes the noun to represent multiple objects. """
	indexLast = len(string)-1
	if string[indexLast] == "y" and string[indexLast-1] not in ["a", "e", "i", "o", "u"]:
		string = string[0:indexLast]
		string += "ies"
	elif string[indexLast] == "f":
		string = string[0:indexLast]
		string += "ves"
	elif string[indexLast-1: indexLast +1] == "fe":
		string = string[0:indexLast-1]
		string += "ves"
	elif string[indexLast] == "s":
		if string[indexLast-1] in ["a", "e", "i", "o", "u"]: string += "s"
		string += "es"
	else:
		string += "s"
	return string
def generate_title_element():
	""" Generates a title element consisting of a noun and random additional elements """
	result = ""
	if chance_out_of(3,4):	# adjective? noun
		if flip_coin():
			result += random_elem(movieTitleAdnouns + movieTitleDoubles)
			result += " "
		result += random_elem(movieTitleNouns + movieTitleDoubles)
		if chance_out_of(1,4): 		# adjective? nouns
			result = make_multiple(result)
	elif flip_coin():			# noun is adjective
		result += random_elem(movieTitleNouns + movieTitleDoubles)
		if chance_out_of(3,4):
			result += " is "
		else: 						# nouns are adjective
			result = make_multiple(result)
			result += " are "
		result += random_elem(movieTitleAdnouns)
	elif flip_coin():			# concept of nouns
		result += random_elem(movieTitleConcepts) + " of " + random_elem(movieTitleNouns + movieTitleDoubles)
		result = make_multiple(result)
	else:							# noun of concept
		result += random_elem(movieTitleObjects + movieTitleDoubles) + " of " + random_elem(movieTitleConcepts)
		if chance_out_of(1,4): 		# noun of concepts
			result = make_multiple(result)
	return result
			def generate_movie_title():	""" Generates a (somewhat plausible) movie title. """	result = ""
	if flip_coin(): result += random_elem(["The", "The", "The", "Beyond", "Way of the", "Life of the",]) + " "
		if chance_out_of(1, 4):	# Title & title
		result += generate_title_element()		result += " " + random_elem(["after", "beyond", "through", "with", "Vs", "and", "&", "despite"]) + " "
			result += generate_title_element()		if flip_coin() or len(result) < 20:	# number? : Subtitle		if flip_coin(): result += " " + str(rng.randint(2, 6)) 		result += ": "		if flip_coin(): result += random_elem(movieSubtitleStarts) + " "
		result += generate_title_element()		if (flip_coin() and len(result) < 50) or len(result) < 30 : result += " " + random_elem(movieSubtitleEnds) 			return resultfor x in range(0, 10):	print( generate_movie_title())