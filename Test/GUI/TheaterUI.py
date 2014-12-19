import tkinter
import tkinter.ttk
import datetime
import Project
import tkhelpers
from SelectTableFrame import *
from NewUserFrame import *
from NewMovieFrame import *

class MainFrame(tkinter.Frame):              
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.theater = Project.Theater('UGC')
        self.master.title(self.theater.name + ' management')
        self.createWidgets()

    def createWidgets(self):
        """ Creates the root frame's widgets. """

        self.tableButton = tkinter.Button(self, text='Change table type')
        self.tableButton.grid()
        self.newUserButton = tkinter.Button(self, text='Register User', command=self.registerUser)
        self.newUserButton.grid()
        self.newMovieButton = tkinter.Button(self, text='Register Movie', command=self.registerMovie)
        self.newMovieButton.grid()
        self.quitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def registerUser(self):
        """ Registers a new user. """

        tkhelpers.showWindow(NewUserFrame, self.theater.register_customer)

    def registerMovie(self):
        """ Registers a new movie. """

        tkhelpers.showWindow(NewMovieFrame, self.theater.register_movie)

def getNow():
    currentTime = datetime.datetime.now()
    return Project.DateTime(Project.Date(currentTime.day, currentTime.month, currentTime.year), Project.Time(currentTime.hour, currentTime.minute, currentTime.second))

root = tkinter.Tk()
app = MainFrame(root)
mdb = app.theater.register_customer("Marc", "De Bel", "marc.debel@bookoutlet.be")
nowTime = getNow()
app.theater.build_auditorium(10)
movie = app.theater.register_movie("Guardians of the Galaxy", 4)
movie = app.theater.find_movie(movie.title)
showtime = app.theater.schedule_showtime(app.theater.auditoria[0], movie, Project.DateTime(getNow().date, app.theater.timeslots[0]))
app.theater.reservations.queue_reservation(Project.ReservationRequest(mdb, app.theater.showtimes[0], 2, nowTime))
app.theater.reservations.process_reservations()
showtime.redeem_ticket(app.theater, mdb)
showtime.redeem_ticket(app.theater, mdb)
root.mainloop()