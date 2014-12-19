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
        self.hashbox = tkinter.ttk.Combobox(self, width = 100, values = ["Unsorted list", "Binary Tree", "Separate Chaining Hashtable/Binary Trees", "Linear Open Addressing Hashtable", "Quadratic Open Addressing Hashtable"])
        self.hashbox.current(0)
        self.hashbox.grid()
        self.quitButton = tkinter.Button(self, text='Accept', command=self.quit)
        self.quitButton.grid()

    def createTable(self):
        index = self.hashbox.current()
        if index == 0:
            return Project.ListTable(Project.DefaultRecordMap(), Project.ArrayList())
        elif index == 1:
            return Project.TreeTable(Project.BinarySearchTree(Project.DefaultRecordMap()))
        elif index == 2:
            return Project.Hashtable(Project.DefaultRecordMap(), Project.BinaryTreeTableFactory())
        elif index == 3:
            return Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(1))
        else:
            return Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(2))