import tkinter
import tkinter.ttk
import tkinter.messagebox
import datetime
import Project
import tkhelpers

class NewMovieFrame(tkinter.Frame):   
    """ A frame that allows for new movies to be created. """
               
    def __init__(self, Callback, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Create movie')
        self.closeCallback = Callback
        self.createWidgets()

    def close(self):
        """ Closes the window, and calls the callback with the information procured by this dialog. """

        title = self.titleEntry.get()
        if not tkhelpers.isEmptyOrWhitespace(title):
            rating = self.ratingEntry.getValue()
            if rating is not None and rating <= 5 and rating >= 0:
                self.closeCallback(title, rating)
                self.master.destroy()
            else:
                tkinter.messagebox.showerror("Whoops?", "The rating field must contain a real number between 0 and 5.")
        else:
            tkinter.messagebox.showerror("Whoops?", "The title field may be empty.")

    def createWidgets(self):
        # Title column
        titleCol = tkinter.Frame(self)
        titleCol.grid()

        # Create a label that says "Movie title"
        titleLabel = tkinter.Label(titleCol, text = "Movie title: ")
        titleLabel.pack(side = tkinter.LEFT)
   
        # Create an entry widget for the title
        self.titleEntry = tkinter.Entry(titleCol, width = 50)
        self.titleEntry.pack(side = tkinter.LEFT)

        # Rating column
        ratingCol = tkinter.Frame(self)
        ratingCol.grid()

        # Create a label that says "Rating"
        ratingLabel = tkinter.Label(ratingCol, text = "Rating: ")
        ratingLabel.pack(side = tkinter.LEFT)
   
        # Create an entry widget for the rating
        self.ratingEntry = tkhelpers.NumberEntry(ratingCol, False, width = 50)
        self.ratingEntry.pack(side = tkinter.LEFT)

        self.acceptButton = tkinter.Button(self, text='Accept', command=self.close)
        self.acceptButton.grid()