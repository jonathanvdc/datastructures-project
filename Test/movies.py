import random

rng = random.Random()

movieTitleParts = ["Hot", "Cold", "Light", "Dawn", 
				   "Gone", "Big", "Burn", "Reading", 
				   "Heat", "Story", "Bourne", "Legacy", 
				   "Sasha", "Russia", "Red", "Blood",
				   "Dark", "Fear", "Death", "Pacific", 
				   "Bold", "Horrible", "America", "Interview",
				   "Truth", "True", "Grit", "Elysium", "Panama", 
				   "Ninja", "Cyborg", "Cop", "Shark",
				   "Murder", "Shank", "Robot", "Machine",
				   "Monster", "Alien", "Thing", "Predator",
				   "Snake", "Peace", "Ghost", "Guns", "Solid",
				   "Metal", "Gear", "Phantom", "Battle", "Tendency",
				   "Diamond", "Unbreakable", "Golden", "Stone", "Steel",
				   "Pain", "Blade", "Godfather", "Odyssey", "Space",
				   "Walker", "Liberty", "Boss", "Boyhood", "Hobbit"]
				   
movieSubtitleStarts = ["Revenge of", "Attack of", "Return of",
							"Story of", "A Tale of", "Requiem for", "A New",
							"End of", "Eternal Sunshine of", "Call for", "Call of",
							"Death of", "Passion of", "Memories of", "The Phantom",
							"Sons of the", "Guns of the", "Prepare for", "The Missing", "Lost",
							"A Dystopian", "Unlimited", "Grandpa's", "A Space", "The Dark",
							"The Smell of", "The Final", "Enter the", "The Usual", "The Big"]
						
movieSubtitleEnds = ["Strikes Back", "Harder", "Menace", "Awakens", 
							"Annihilation", "of Power", "of Fury", "With a Cause",
							"Again", "Better", "Faster", "Stronger", "Justice",
							"Wizard", "Redemption", "Revengeance", "Eater", "of Liberty",
							"from Space", "from Beneath", "from Hell", "After Dark"]
						
def flip_coin():
	return rng.randint(0, 1) == 1

def random_elem(sequence):
	return sequence[rng.randrange(0, len(sequence))]

def random_list_elem(collection):
	index = rng.randrange(0, collection.count)
	for i, item in enumerate(collection):
		if i == index:
			return item

def generate_movie_title():
	""" Generates a (somewhat plausible) movie title. """
	result = ""
	if flip_coin():
		result += "The "
	for i in range(0, rng.randint(0, 1)):
		result += random_elem(movieTitleParts) + " "
		result += random_elem(["of ", "after ", "beyond ", "through ", "with ", "vs ", "and ", "is ", "", ""])
	result += random_elem(movieTitleParts)
	
	if flip_coin():
		end = False
		if flip_coin(): result += " " + str(rng.randint(2, 5)) 
		result += ": "
		if flip_coin():
			result += random_elem(movieSubtitleStarts) + " "
		else:
			end = True
		
		result += random_elem(movieTitleParts)
		
		if flip_coin() or end: result += " " + random_elem(movieSubtitleEnds) 
		
		random_elem(movieTitleParts)
	return result

for x in range(0, 10):
	print( generate_movie_title())
