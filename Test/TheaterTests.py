import sys
import random
sys.path.append('..\Implementations')

import Project

theater = Project.Theater("Kinepolis")

rng = random.Random()
firstNames = ["John", "Marion", "Amanda", "Allison",
              "Jesus", "Evans", "Dexter", "Maria",
              "Andrew", "Greg", "Consuela", "Tom",
              "Martha", "Angela", "Jack", "Snake", "George"]
lastNames = ["Doe", "Jones", "Williams", "Smith", "Taylor", 
             "Walker", "Gonzalez", "Mitchell", "Collins",
             "Stewart", "Morgan", "Morrison", "Zane",
             "Jolie", "Plisskin", "Freeman", "Stanza"]
movieTitleParts = ["Hot", "Cold", "Light", "Dawn", 
                   "Gone", "Big", "Burn", "Reading", 
                   "Heat", "Story", "Bourne", "Legacy", 
                   "Sasha", "Russia", "Red", "Blood",
                   "Dark", "Fear", "Death", "Pacific", 
                   "Bold", "Horrible", "America", "Interview",
                   "True", "Grit", "Elysium", "Panama", 
                   "Ninja", "Cyborg", "Cop", "Shark",
                   "Murder", "Blood", "Shank", "Dark"]
                   
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

def create_random_list():
    if rng.randint(0, 1) == 1:
        return Project.LinkedList()
    else:
        return Project.ArrayList()

def random_dateTime():
    """ Generates a random DateTime instance """
    return Project.DateTime(Project.Date(12, 19, 2014), Project.Time(rng.randint(0, 23), rng.randint(0, 60)))

def create_users():
    """ Creates random users """
    print("Creating users...")
    for i in range(0, 30):
        first = random_elem(firstNames)
        last = random_elem(lastNames)
        theater.register_customer(first, last, first.lower() + "." + last.lower() + "@outlook.com")
        theater.registered_customers.swap(create_random_list())
    for item in theater.registered_customers:
        print(str(item))

def create_movies():
    """ Creates random movies """
    print("Creating movies...")
    for i in range(0, 20):
        theater.register_movie(generate_movie_title(), rng.randint(0, 10) / 2)
    for item in theater.movies:
        print(str(item))

def create_auditoria():
    """ Creates random auditoria """
    print("Creating auditoria...")
    for i in range(0, 5):
        theater.build_auditorium(rng.randint(10, 100))

def create_timeslots():
    """ Creates random timeslots """
    print("Creating timeslots...")
    i = 0
    while i < 6:
        time = Project.Time(rng.randint(0, 23), rng.randint(0, 60))
        noInsert = False
        for slot in theater.timeslots:
            if slot == time:
                noInsert = True
                break
        if not noInsert:
            theater.timeslots.add(time)
            i += 1

def create_showtimes():
    """ Creates random showtimes """
    print("Creating showtimes...")
    for i in range(0, 100):
        theater.schedule_showtime(random_list_elem(theater.auditoria), random_list_elem(theater.movies), Project.DateTime(Project.Date(12, 19, 2014), random_list_elem(theater.timeslots)))
    # number of possible showtimes = number of auditoria * number of timeslots = 10 * 5 = 50 < 100
    assert(theater.showtimes.count <= 50)

def reserve_tickets():
    """ Makes random reservations. """
    print("Reserving tickets...")
    for i in range(0, 300):
        theater.reservations.queue_reservation(Project.ReservationRequest(random_list_elem(theater.registered_customers), random_list_elem(theater.showtimes), rng.randint(0, 100), random_dateTime()))
    theater.reservations.process_reservations()
    # Will always fail
    theater.reservations.queue_reservation(Project.ReservationRequest(theater.reservations.reservations[0].customer, theater.reservations.reservations[0].showtime, theater.reservations.reservations[0].showtime.number_of_free_seats + 1, random_dateTime()))
    assert(theater.reservations.process_reservations().count == 0)

def redeem_tickets():
    """ Redeems all tickets """
    print("Redeeming tickets...")
    ids = [theater.showtimes.key_map.map(elem) for elem in theater.showtimes]
    notStartedCount = 0
    for i in ids:
        item = theater.showtimes[i]
        redeemed = False
        originalCount = theater.showtimes.count
        for user in theater.registered_customers:
            while item.has_ticket(user):
                item.redeem_ticket(theater, user)
                redeemed = True
        print("All tickets redeemed for " + str(item))
        if not redeemed:
            assert(theater.showtimes.count == originalCount)
            notStartedCount += 1
        else:
            assert(theater.showtimes.count == originalCount - 1)
    # Showtimes whose tickets have all been redeemed should start at this point
    assert(theater.showtimes.count == notStartedCount)

def main():
    create_timeslots()
    create_auditoria()
    create_movies()
    create_users()
    create_showtimes()
    reserve_tickets()
    redeem_tickets()
    print("All tests completed")

main()
