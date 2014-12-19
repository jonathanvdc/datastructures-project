from Dialogs import *
import Project

theater = Project.Theater("Kinepolis")

done = False
def quitDialogs():
    global done
    done = True

mainDialog = MenuDialog("MainDialog", "Welcome to the theater management menu for " + theater.name)
mainDialog.add_option(NewUserDialog(theater.register_customer))
mainDialog.add_option(NewMovieDialog(theater.register_movie))
mainDialog.add_option(NewShowtimeDialog(theater))
mainDialog.add_option(QuitDialog(quitDialogs))
mainDialog.add_option(CollectionDialog("view movies", "Movies currently playing:", theater.movies))
mainDialog.add_option(CollectionDialog("view timeslots", "Current timeslots:", theater.timeslots))
mainDialog.add_option(CollectionDialog("view showtimes", "Current showtimes:", theater.showtimes))
while not done:
    mainDialog.RunDialog() # Run this dialog. Forever.