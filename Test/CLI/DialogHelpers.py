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

    # Tree table with User -> str (Name) map
    customerTable = Project.TreeTable(Project.BinarySearchTree(Project.UserNameMap()))
    for item in Theater.registered_customers:
        customerTable.insert(item)

    selectCustomerDialog = OptionDialog("select customer", Text, customerTable)
    return selectCustomerDialog.RunDialog()

def SelectStartTime(Theater, Auditorium):
    """ Selects a start time for a showtime in the given auditorium at the given theater. """

    return ShowtimeStartDialog(Theater, Auditorium).RunDialog()