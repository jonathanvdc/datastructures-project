from CommandLineDialog import *
from OptionDialog import *
from ShowtimeStartDialog import *
import Project

def SelectMovie(Theater, Text):
    """ Selects a movie from the theater's catalog. """

    movieTable = Project.Hashtable(Project.MovieTitleMap(), Project.BinaryTreeTableFactory())
    for item in Theater.movies:
        movieTable.insert(item)
    selectMovieDialog = OptionDialog("select movie", Text, movieTable)
    return selectMovieDialog.RunDialog()

def SelectAuditorium(Theater, Text):
    """ Selects an auditorium from the theater's catalog. """

    # Tree table with Auditorium -> str map
    auditoriumTable = Project.TreeTable(Project.BinarySearchTree(Project.ToStringMap()))
    for item in Theater.auditoria:
        auditoriumTable.insert(item)

    selectAuditoriumDialog = OptionDialog("select auditorium", Text, auditoriumTable)
    return selectAuditoriumDialog.RunDialog()

def SelectCustomer(Theater, Text):
    """ Selects a customer from the theater's group of customers """

    if Theater.registered_customers.count == 0:
        print("Cannot select customer: no customers have been registered yet.")
        return None

    # Tree table with User -> str (Name) map
    customerTable = Project.TreeTable(Project.BinarySearchTree(Project.UserNameMap()))
    for item in Theater.registered_customers:
        customerTable.insert(item)

    selectCustomerDialog = OptionDialog("select customer", Text, customerTable)
    return selectCustomerDialog.RunDialog()

def SelectTimeslot(Candidates, Text):
    """ Selects a timeslot from a collection of candidates. """

    if Candidates.count == 0:
        print("Could not select a timeslot because no timeslots have been defined.")
        return None

    # Linear open-addressed hash table with time -> time map
    timeslotTable = Project.OpenHashtable(Project.IdentityMap(), Project.PowerSequenceMap(1))
    for slot in Candidates:
        timeslotTable.insert(slot)

    selectTimeslotDialog = OptionDialog("select timeslot", Text, timeslotTable)
    # Reads times as keys
    selectTimeslotDialog.ReadOptionKey = selectTimeslotDialog.ReadTime
    return selectTimeslotDialog.RunDialog()

def SelectStartTime(Theater, Auditorium):
    """ Selects a start time for a showtime in the given auditorium at the given theater. """

    return ShowtimeStartDialog(Theater, Auditorium).RunDialog()

def SelectShowtime(Candidates):
    """ Selects a showtime from the pool of candidates. """

    if Candidates.count == 0:
        print("No showtimes have been scheduled yet.")
        return None

    # Quadratic open-addressed hashtable with default Record -> Key map
    showtimes = Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(2))
    for item in Candidates:
        showtimes.insert(item)

    showtimeDialog = OptionDialog("select showtime", "Please select a showtime", showtimes, True)
    showtimeDialog.ReadOptionKey = showtimeDialog.ReadIndex
    return showtimeDialog.RunDialog()