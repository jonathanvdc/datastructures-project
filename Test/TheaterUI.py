import tkinter
import tkinter.ttk
import datetime
import Project

class SelectTableFrame(tkinter.Frame):              
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Select table type')
        self.createWidgets()

    def createWidgets(self):
        self.hashbox = tkinter.ttk.Combobox(self, values = ["Binary Tree", "Separate Chaining Hashtable/Binary Trees", "Linear Open Addressing Hashtable", "Quadratic Open Addressing Hashtable"])
        self.hashbox.current(0)
        self.hashbox.grid()
        self.quitButton = tkinter.Button(self, text='Accept', command=self.quit)
        self.quitButton.grid()

    def createTable(self):
        index = self.hashbox.current()
        if index == 0:
            return Project.TreeTable(Project.BinarySearchTree(Project.DefaultRecordMap()))
        elif index == 1:
            return Project.Hashtable(Project.DefaultRecordMap(), Project.BinaryTreeTableFactory())
        elif index == 2:
            return Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(1))
        else:
            return Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(2))

class NewUserFrame(tkinter.Frame):              
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Register user')
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tkinter.Button(self, text='Accept', command=self.quit)
        self.quitButton.grid()

class MainFrame(tkinter.Frame):              
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.theater = Project.Theater('UGC')
        self.master.title(self.theater.name + ' management')
        self.createWidgets()

    def createWidgets(self):
        self.tableButton = tkinter.Button(self, text='Change table type')
        self.tableButton.grid()
        self.quitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

def getNow():
    currentTime = datetime.datetime.now()
    return Project.DateTime(Project.Date(currentTime.day, currentTime.month, currentTime.year), Project.Time(currentTime.hour, currentTime.minute, currentTime.second))

app = MainFrame()
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
app.mainloop()
print(table)