from CommandLineDialog import *
from OptionDialog import *
from ShowtimeStartDialog import *
from TypeBucketFactory import *
import Project

def SelectMovie(Dialog, Theater, Text):
    """ Selects a movie from the theater's catalog. """

    movieTable = Project.Hashtable(Project.MovieTitleMap(), Project.BinaryTreeTableFactory())
    for item in Theater.movies:
        movieTable.insert(item)
    selectMovieDialog = OptionDialog("select movie", Text, movieTable)
    return selectMovieDialog.RunDialog(Dialog)

def SelectAuditorium(Dialog, Theater, Text):
    """ Selects an auditorium from the theater's catalog. """

    # Tree table with Auditorium -> str map
    auditoriumTable = Project.TreeTable(Project.BinarySearchTree(Project.DefaultRecordMap()))
    for item in Theater.auditoria:
        auditoriumTable.insert(item)

    selectAuditoriumDialog = OptionDialog("select auditorium", Text, auditoriumTable, True)
    selectAuditoriumDialog.ReadOptionKey = selectAuditoriumDialog.ReadIndex
    return selectAuditoriumDialog.RunDialog(Dialog)

def SelectCustomer(Dialog, Theater, Text):
    """ Selects a customer from the theater's group of customers """

    if Theater.registered_customers.count == 0:
        Dialog.Write("Cannot select customer: no customers have been registered yet.")
        return None

    # Tree table with User -> str (Name) map
    customerTable = Project.TreeTable(Project.BinarySearchTree(Project.UserNameMap()))
    for item in Theater.registered_customers:
        customerTable.insert(item)

    selectCustomerDialog = OptionDialog("select customer", Text, customerTable)
    return selectCustomerDialog.RunDialog(Dialog)

def SelectTimeslot(Dialog, Candidates, Text):
    """ Selects a timeslot from a collection of candidates. """

    if Candidates.count == 0:
        Dialog.Write("Could not select a timeslot because no timeslots have been defined.")
        return None

    # Linear open-addressed hash table with time -> time map
    timeslotTable = Project.OpenHashtable(Project.IdentityMap(), Project.PowerSequenceMap(1))
    for slot in Candidates:
        timeslotTable.insert(slot)

    selectTimeslotDialog = OptionDialog("select timeslot", Text, timeslotTable)
    # Reads times as keys
    selectTimeslotDialog.ReadOptionKey = selectTimeslotDialog.ReadTime
    return selectTimeslotDialog.RunDialog(Dialog)

def SelectStartTime(Dialog, Theater, Auditorium):
    """ Selects a start time for a showtime in the given auditorium at the given theater. """

    return ShowtimeStartDialog(Theater, Auditorium).RunDialog(Dialog)

def SelectShowtime(Dialog, Candidates):
    """ Selects a showtime from the pool of candidates. """

    if Candidates.count == 0:
        Dialog.Write("No showtimes have been scheduled yet.")
        return None

    # Quadratic open-addressed hashtable with default Record -> Key map
    showtimes = Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(2))
    for item in Candidates:
        showtimes.insert(item)

    showtimeDialog = OptionDialog("select showtime", "Please select a showtime", showtimes, True)
    showtimeDialog.ReadOptionKey = showtimeDialog.ReadIndex
    return showtimeDialog.RunDialog(Dialog)

def GetTableDelegates():
    """ Gets a table of key-value pairs of names and delegates that create new tables. """

    table = Project.TreeTable(Project.TwoThreeFourSearchTree(Project.DefaultRecordMap()))

    table.insert(Project.KeyValuePair("list table - array", lambda map: Project.ListTable(map, Project.ArrayList())))
    table.insert(Project.KeyValuePair("list table - linked list", lambda map: Project.ListTable(map, Project.LinkedList())))
    table.insert(Project.KeyValuePair("binary tree table", lambda map: Project.TreeTable(Project.BinarySearchTree(map))))
    table.insert(Project.KeyValuePair("2-3-4 tree table", lambda map: Project.TreeTable(Project.TwoThreeFourSearchTree(map))))
    table.insert(Project.KeyValuePair("separate chaining hashtable - binary tree", lambda map: Project.Hashtable(map, Project.BinaryTreeTableFactory())))
    table.insert(Project.KeyValuePair("separate chaining hashtable - 2-3-4 tree", lambda map: Project.Hashtable(map, TypeBucketFactory(Project.TwoThreeFourSearchTree))))
    table.insert(Project.KeyValuePair("separate chaining hashtable - array list", lambda map: Project.Hashtable(map, TypeBucketFactory(lambda bucket_map: Project.ListTable(bucket_map, Project.ArrayList())))))
    table.insert(Project.KeyValuePair("separate chaining hashtable - linked list", lambda map: Project.Hashtable(map, TypeBucketFactory(lambda bucket_map: Project.ListTable(bucket_map, Project.LinkedList())))))
    table.insert(Project.KeyValuePair("linear open addressing hashtable", lambda map: Project.OpenHashtable(map, Project.PowerSequenceMap(1))))
    table.insert(Project.KeyValuePair("quadratic open addressing hashtable", lambda map: Project.OpenHashtable(map, Project.PowerSequenceMap(2))))

    return table