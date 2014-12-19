import sys
sys.path.append('..\..\Implementations')

from Dialogs import *
import Project

theater = Project.Theater("Kinepolis")
theater.build_auditorium(10)
theater.register_movie("Guardians of the Galaxy", 4.0)

done = False
def quitDialogs():
    global done
    done = True

def createSettings():
    settingsDialog = MenuDialog("settings", "Select an option to change the settings associated with it.")
    settingsDialog.add_option(SwapBackingListDialog("swap auditoria backing list", theater.auditoria))
    return settingsDialog

mainDialog = MenuDialog("main dialog", "Welcome to the theater management menu for " + theater.name, Project.TreeTable(Project.BinarySearchTree(Project.DefaultRecordMap())))
mainDialog.add_option(NewUserDialog(theater.register_customer))
mainDialog.add_option(NewMovieDialog(theater.register_movie))
mainDialog.add_option(NewShowtimeDialog(theater))
mainDialog.add_option(NewTimeslotDialog(theater))
mainDialog.add_option(ReserveTicketDialog(theater))
mainDialog.add_option(RedeemTicketDialog(theater))

mainDialog.add_option(QuitDialog(quitDialogs))

mainDialog.add_option(CollectionDialog("view movies", "Movies currently playing:", theater.movies))
mainDialog.add_option(CollectionDialog("view timeslots", "Current timeslots:", theater.timeslots))
mainDialog.add_option(CollectionDialog("view showtimes", "Current showtimes:", theater.showtimes))
mainDialog.add_option(CollectionDialog("view auditoria", "Current auditoria:", theater.auditoria))
mainDialog.add_option(CollectionDialog("view users", "Current users:", theater.registered_customers))

mainDialog.add_option(createSettings())

mainDialog.add_option(DeleteTimeslotDialog(theater))

while not done:
    mainDialog.RunDialog() # Run this dialog. Forever.