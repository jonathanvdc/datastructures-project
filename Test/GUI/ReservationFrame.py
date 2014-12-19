import tkinter
import tkinter.ttk
import tkinter.messagebox
import datetime
import Project
import tkhelpers

class ReservationFrame(tkinter.Frame):   
    """ A frame that allows for new reservations to be created. """
               
    def __init__(self, Theater, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Make a reservation')
        self.theater = Theater
        self.createWidgets()

    def close(self):
        """ Closes the window, and calls the callback with the information procured by this dialog. """

        self.master.destroy()

    def createWidgets(self):
        # First name column
        showtimeCol = tkinter.Frame(self)
        showtimeCol.grid()

        # Create a label that says "Select showtime"
        showtimeLabel = tkinter.Label(showtimeCol, text = "Select showtime: ")
        showtimeLabel.pack(side = tkinter.LEFT)
        
        # Create an combobox widget for the showtime
        self.showtimeCombo = tkhelpers.ShowtimeComboBox(showtimeCol, self.theater)
        self.showtimeCombo.pack(side = tkinter.LEFT)

        self.acceptButton = tkinter.Button(self, text='Make reservation', command=self.close)
        self.acceptButton.grid()