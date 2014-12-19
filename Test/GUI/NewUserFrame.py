import tkinter
import tkinter.ttk
import tkinter.messagebox
import datetime
import Project
import tkhelpers

class NewUserFrame(tkinter.Frame):   
    """ A frame that allows for new users to be created. """
               
    def __init__(self, Callback, master=None):
        tkinter.Frame.__init__(self, master)   
        self.grid()
        self.master.title('Register user')
        self.closeCallback = Callback
        self.createWidgets()

    def close(self):
        """ Closes the window, and calls the callback with the information procured by this dialog. """
        firstName, lastName = self.firstNameEntry.get(), self.lastNameEntry.get()
        if tkhelpers.isEmptyOrWhitespace(firstName) or tkhelpers.isEmptyOrWhitespace(lastName):
            tkinter.messagebox.showerror("Whoops?", "Neither first name nor last name fields may be empty.")
        else:
            self.closeCallback(firstName, lastName, self.emailEntry.get())
            self.master.destroy()

    def createWidgets(self):
        # First name column
        firstNameCol = tkinter.Frame(self)
        firstNameCol.grid()

        # Create a label that says "First name"
        firstNameLabel = tkinter.Label(firstNameCol, text = "First name: ")
        firstNameLabel.pack(side = tkinter.LEFT)
   
        # Create an entry widget for the first name
        self.firstNameEntry = tkinter.Entry(firstNameCol, width = 49)
        self.firstNameEntry.pack(side = tkinter.LEFT)

        # Last name column
        lastNameCol = tkinter.Frame(self)
        lastNameCol.grid()

        # Create a label that says "Last name"
        lastNameLabel = tkinter.Label(lastNameCol, text = "Last name: ")
        lastNameLabel.pack(side = tkinter.LEFT)
   
        # Create an entry widget for the last name
        self.lastNameEntry = tkinter.Entry(lastNameCol, width = 50)
        self.lastNameEntry.pack(side = tkinter.LEFT)

        # E-mail column
        emailCol = tkinter.Frame(self)
        emailCol.grid()

        # Create a label that says "E-mail address"
        emailLabel = tkinter.Label(emailCol, text = "E-mail address: ")
        emailLabel.pack(side = tkinter.LEFT)
   
        # Create an entry widget for the e-mail address
        self.emailEntry = tkinter.Entry(emailCol, width = 46)
        self.emailEntry.pack(side = tkinter.LEFT)

        self.acceptButton = tkinter.Button(self, text='Accept', command=self.close)
        self.acceptButton.grid()