import randomrng = random.Random()
# Collection of nouns that describe concepts
movieTitleConcepts = [ "Life", "Death", "Power", "Strength", "Wisdom", "Defiance", "Truth",
							"Acceptance", "Forgiveness", "Murder", "Terror", "Liberty",
							"Joy", "Sorrow", "Fury", "Fear", "Pain", "War", "Honor", "Duty", "Guardian"]

# Collection of nouns that describe objects
movieTitleObjects = 	[ "Dawn", "Burn", "Story", "Legacy", "Birth", "Galaxy", "Guardian", "Hero",
							"Interview",  "Grit", "Cop", "Shark", "Room", "Fight", "Knife", "America",
							"Shank", "Thing", "Snake", "Gun", "Gear", "Tendency", "Sword", "Russia",
							"Blade", "Godfather", "Odyssey", "Walker", "Boyhood", "Activity", "Lie",
							"Massacre", "Chainsaw", "Eater", "Fist", "Werewolf", "Vampire", "Boss",
							"Crusader", "Rise", "Planet", "Ape", "Germany", "Hitler", "Stalin"]
# Collection of nounsmovieTitleNouns = movieTitleConcepts + movieTitleObjects
# Collection of adjectivesmovieTitleAdnouns = [ "Hot", "Cold", "Light", "Gone", "Big",  "Dark", "Pacific", "Bold", 							"Horrible", "True", "Solid", "Golden", "Red", "Scary", "Paranormal",
							"Black", "Unbreakable", "American", "Russian", "Righteous", "Heroic",
							"Dangerous", "Lethal", "Global", "Viral", "Real", "Bloody", "Gory", "Deadly",
							"Deep-Space", "Violent", "Large"]# Collection of nouns that double as adjectives, and adjectives that double as nounsmovieTitleDoubles = [ "Alien", "Liberty", "Hobbit", "Monster", "Robot", "American", "Russian",							"Cyborg", "Ninja", "Machine", "Predator", "Stone", "Steel", "Space", 							"Diamond", "Metal", "Fear", "Death", "Blood", "Heat", "Fallen", 							"Peace", "Ghost", "Phantom", "Battle", "Enemy", "Hostile", "Expendable",
							"Mutant", "Nightmare", "Texas", "Stardust", "German", "Nazi", "Communist",
							"Socialist"]
							

							
# Collection of starts to a movie subtitlemovieSubtitleStarts = ["Revenge of the", "Attack of the", "Return of the", "Electric",							"Story of the", "A Tale of the", "Requiem for a", "A New",							"End of the", "Eternal Sunshine of the", "Call for", "Call of",							"Death of the", "Passion of the", "Memories of", "The Phantom",							"Sons of the", "Guns of the", "Prepare for", "The Missing", "The Lost",							"A Dystopian", "Unlimited", "Grandpa's", "A Space", "The Dark",							"The Smell of", "The Final", "Enter the", "The Usual", "The Big"]

# Collection of ends to a movie subtitlemovieSubtitleEnds = ["Strikes Back", "Harder", "Menace", "Awakens", "Boogaloo",							"Annihilation", "of Power", "of Fury", "With a Cause",							"Again", "Better", "Faster", "Stronger", "Justice",							"Wizard", "Redemption", "Vengeance", "of Liberty",							"from Space", "from Beneath", "from Hell", "After Dark"]
						
# Collection of starts to a unique name						
nameStarts = ["Spider", "Bat", "Super", "Monster", "Über", "Ultra", "Mega", "Acid", "Aether", "Anthro",
							"Xeno", "Trans", "Shark", "Bull", "Swap", "Octo", "Cyclops", "Aqua", "Auto", "Caust",
							"Dextro", "Dino", "Tyranno", "Extreme", "Fungus", "Geo", "Ichtyo", "Infra", "Inter", "Kilo",
							"Klepto", "Libero", "Logi", "Macro", "Mania", "Mecha", "Micro", "Necro", "Nocto", "Quad", "Arachno",
							"Termi", "Than", "Torpe", "Ultima", "Solid", "Liquid", "Psycho", "Robo"]
# Collection of ends to a unique name
nameEnds = ["man", "-Man", "woman", "-Woman", "dude", "guy", "friend", "monster", "topus", "bowski", "zilla",
							"-Thing", "mutant", " Mutant", "ator", "former", "beast", "oid", "cano", "nado", "saur",
							" Snake", "shark", "cop"]						def chance_out_of(x, y):
	""" Has X chance out of Y to return True. """	return rng.randint(1, y) <= x						def flip_coin():
	""" Has 1 chance out of 2 to return True. """	return chance_out_of(1, 2)def random_elem(list):
	""" Returns a random element from a given list. """	return list[rng.randrange(0, len(list))]
	
def is_vowel(char):
	return char in ["a", "e", "i", "o", "u"]
	
	
def make_multiple(string):
	""" Takes a string ending in a noun and changes the noun to represent multiple objects. """
	indexLast = len(string)-1
	if string[indexLast] == "y" and not is_vowel(string[indexLast-1]):
		string = string[0:indexLast]
		string += "ies"
	elif string[indexLast] == "f":
		string = string[0:indexLast]
		string += "ves"
	elif string[indexLast-1: indexLast +1] == "fe":
		string = string[0:indexLast-1]
		string += "ves"
	elif string[indexLast] == "o":
		string += "es"
	elif string[indexLast] == "s":
		if is_vowel(string[indexLast-1]): string += "s"
		string += "es"
	else:
		string += "s"
	return string
	
def generate_unique_name():
	""" Generates a unique name for a fictional concept. """
	name = random_elem(nameStarts)
	end = random_elem(nameEnds)
	if is_vowel(name[len(name)-1] ) and is_vowel(end[0]): name += "n"
	return name + end
def generate_title_element(phrase = True):
	""" Generates a title element consisting of a noun and random additional elements """
	result = ""
	if chance_out_of(3,4):					# adjective? noun
		if flip_coin():
			result += random_elem(movieTitleAdnouns + movieTitleDoubles)
			result += " "
		result += random_elem(movieTitleNouns + movieTitleDoubles)
		if chance_out_of(1,4): 					# adjective? nouns
			result = make_multiple(result)
	elif flip_coin() and phrase:			# noun is adjective
		result += random_elem(movieTitleNouns + movieTitleDoubles)
		if chance_out_of(3,4):
			result += " is "
		else: 										# nouns are adjective
			result = make_multiple(result)
			result += " are "
		result += random_elem(movieTitleAdnouns)
	elif flip_coin():							# concept of nouns
		result += random_elem(movieTitleConcepts) + " of " + random_elem(movieTitleNouns + movieTitleDoubles)
		result = make_multiple(result)
	else:											# noun of concept
		result += random_elem(movieTitleObjects + movieTitleDoubles) + " of " + random_elem(movieTitleConcepts)
		if chance_out_of(1,4): 					# noun of concepts
			result = make_multiple(result)
	return result
			def generate_movie_title():	""" Generates a (somewhat plausible) movie title. """
	
	unique_name = ""	result = ""
	if chance_out_of(4, 5): 	#Element? connector? Element
		if flip_coin(): result += random_elem(["The", "The", "The", "Beyond", "Way of the", "Life of the"]) + " "		if chance_out_of(1, 4):		# Element connector Element
			result += generate_title_element()			result += " " + random_elem(["after", "beyond the", "through", "with", "Vs", "and the", "&", "despite the"]) + " "		result += generate_title_element( len(result) < 8 )
	
	else:								# Unique name		if flip_coin(): result += "The "
		unique_name = generate_unique_name()
		result += unique_name
		if chance_out_of(1, 4):	# Unique Name connector Unique Name
			result += " " + random_elem(["&", "and", "Versus", "Vs", "Vs.", "with", "featuring", "feat.", "against"]) + " "
			result += generate_unique_name() if flip_coin() else generate_title_element(False)
				if flip_coin() or len(result) < 20:	# Subtitle		if flip_coin(): result += " " + str(rng.randint(2, 6)) 		result += ": "		if flip_coin(): result += random_elem(movieSubtitleStarts) + " "
	
		if flip_coin() or unique_name == "":
			result += generate_title_element(False)
		else:
			result += unique_name
			if (flip_coin() and len(result) < 50) or len(result) < 30 : result += " " + random_elem(movieSubtitleEnds) 			return resultfor x in range(0, 10):	print( generate_movie_title())