import tkinter
import tkinter.ttk
import tkhelpers
import Project

class MovieManagerFrame(tkinter.Frame):
    """ A frame that is inteded for the management of movies. """

    def __init__(self, Theater, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Manage movies')
        self.theater = Theater
        self.createWidgets()

    def createWidgets(self):
        """ Creates the movie manager frame's widgets. """



        self.acceptButton = tkinter.Button(self, text='Done', command=self.close)
        self.acceptButton.grid()